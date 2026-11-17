"""Lógica de evaluación: extrae texto del PDF y lo evalúa con Google Gemini."""
import io
import json
import os
import time

import pypdf

from rubrica import DIMENSIONES, ESCALA, rubrica_texto

MAX_CHARS = int(os.environ.get("MAX_PDF_CHARS", "60000"))
TIMEOUT_IA = int(os.environ.get("TIMEOUT_IA", "90"))
REINTENTOS = int(os.environ.get("REINTENTOS_IA", "3"))

# El modelo principal se toma de GEMINI_MODEL; si da 503 (sobrecarga),
# se prueban los siguientes como respaldo.
MODELO_GEMINI = os.environ.get("GEMINI_MODEL", "gemini-3.1-flash-lite")
MODELOS_RESPALDO = [
    MODELO_GEMINI,
    "gemini-3.5-flash-lite",
]


class ErrorEvaluacion(Exception):
    """Error de negocio para mostrar un mensaje claro al usuario."""


def extraer_texto_pdf(datos_pdf: bytes) -> str:
    """Extrae el texto de un PDF recibido como bytes."""
    try:
        lector = pypdf.PdfReader(io.BytesIO(datos_pdf))
    except Exception as exc:  # noqa: BLE001
        raise ErrorEvaluacion(
            "No se pudo leer el PDF. Verifica que el archivo no esté dañado."
        ) from exc

    partes = []
    for pagina in lector.pages:
        partes.append(pagina.extract_text() or "")
    texto = "\n".join(partes).strip()

    if len(texto) < 50:
        raise ErrorEvaluacion(
            "No se encontró texto en el PDF. Si es un documento escaneado "
            "(imágenes), necesita OCR antes de evaluarlo."
        )

    if len(texto) > MAX_CHARS:
        texto = texto[:MAX_CHARS] + "\n\n[...documento truncado...]"
    return texto


def _esquema() -> dict:
    return {
        "nombre_negocio": "string (nombre del negocio digital si se identifica, o 'No especificado')",
        "resumen_ejecutivo": "string (4-6 frases, con voz de ingeniero de negocios digitales)",
        "puntaje_global": "number 0-100",
        "nivel": "string: Sobresaliente | Sólido | Aceptable | Débil | Insuficiente",
        "veredicto": "string: una frase contundente de inversión/viabilidad (p. ej. apto para inversión, requiere pivote, etc.)",
        "dimensiones": [
            {
                "id": "string (id exacto de la dimensión de la rúbrica)",
                "nombre": "string",
                "puntaje": "number 0-5",
                "justificacion": "string (análisis técnico, no superficial)",
                "fortalezas": ["string"],
                "debilidades": ["string"],
                "recomendaciones": ["string"],
            }
        ],
        "analisis_competitivo": {
            "resumen": "string (panorama del mercado y posición relativa del negocio)",
            "competidores": [
                {
                    "nombre": "string (producto/empresa real y conocida del mercado)",
                    "descripcion": "string (qué hace y a quién atiende)",
                    "similitud": "string (en qué se parece al negocio evaluado)",
                    "ventaja_de_ellos": "string (qué hacen mejor o dónde son fuertes)",
                },
            ],
            "diferenciadores": ["string (qué distingue al negocio evaluado frente a esos competidores)"],
            "ventaja_competitiva_sostenible": "string (si tiene foso/moat defendible y por qué)",
            "posicionamiento": "string: Líder potencial | Retador | Seguidor | Nicho | Sin diferenciación clara",
        },
        "riesgos_principales": ["string"],
        "recomendaciones_prioritarias": ["string"],
    }


def _construir_prompt(texto_negocio: str) -> tuple:
    system = (
        "Actúas como un evaluador profesional e ingeniero de negocios digitales "
        "con experiencia en arquitectura de negocio, estrategia e inversión en "
        "startups. Evalúas con rigor técnico, criterio de inversionista y tono "
        "profesional, objetivo y constructivo. Usas los marcos de la rúbrica "
        "(Modelo de Negocio, Modelo Estratégico, Mapa de Capacidades, Análisis "
        "Estratégico Empresarial y la cascada de decisiones de Playing to Win de "
        "Lafley & Martin). Para el análisis competitivo usas tu conocimiento del "
        "mercado para nombrar productos o empresas reales comparables. Si el "
        "documento no aporta información para un criterio, lo dices explícitamente "
        "y calificas bajo. No inventes datos del negocio que no estén en el "
        "documento, pero SÍ puedes aportar referencias reales de mercado para el "
        "benchmarking."
    )

    user = f"""Evalúa el siguiente negocio digital con estándar profesional.

=== RÚBRICA (dimensiones y criterios) ===
{rubrica_texto()}

=== ESCALA DE CALIFICACIÓN ===
{ESCALA}

=== INSTRUCCIONES ===
1. Califica cada dimensión de 0 a 5 según la escala, con una justificación técnica (no superficial), fortalezas, debilidades y recomendaciones accionables.
2. ANÁLISIS COMPETITIVO (obligatorio): identifica entre 2 y 4 productos o empresas REALES del mercado que sean similares o competidores del negocio evaluado. Para cada uno explica qué hace, en qué se parece y qué hacen mejor. Luego determina qué DIFERENCIA al negocio evaluado, si tiene una ventaja competitiva sostenible (moat) y su posicionamiento.
3. Calcula el puntaje_global (0-100) como promedio ponderado por el peso de cada dimensión, normalizado a 100.
4. Asigna un nivel y un veredicto profesional (tipo decisión de inversión).
5. Lista riesgos principales y recomendaciones prioritarias (máximo 5 de cada una).
6. Responde ÚNICAMENTE con un JSON válido que cumpla EXACTAMENTE este esquema (sin texto adicional, sin markdown):

{json.dumps(_esquema(), ensure_ascii=False, indent=2)}

=== DOCUMENTO DEL NEGOCIO DIGITAL ===
{texto_negocio}
"""
    return system, user


def _normalizar(resultado: dict) -> dict:
    """Asegura que el puntaje global sea consistente con los pesos."""
    pesos = {d["id"]: d["peso"] for d in DIMENSIONES}
    total_peso = sum(pesos.values())

    suma = 0.0
    for dim in resultado.get("dimensiones", []):
        peso = pesos.get(dim.get("id"), 0)
        puntaje = float(dim.get("puntaje", 0) or 0)
        suma += (puntaje / 5.0) * peso

    if total_peso:
        resultado["puntaje_global"] = round(suma / total_peso * 100, 1)
    return resultado


def _limpiar_json(contenido: str) -> str:
    """Quita vallas de markdown que el modelo pueda agregar."""
    c = (contenido or "").strip()
    if c.startswith("```"):
        c = c.split("\n", 1)[1] if "\n" in c else c
        c = c.rsplit("```", 1)[0]
        if c.lstrip().startswith("json"):
            c = c.lstrip()[4:]
    return c.strip()


def evaluar_pdf(datos_pdf: bytes) -> dict:
    """Punto de entrada: PDF en bytes -> diccionario con la evaluación."""
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise ErrorEvaluacion(
            "Falta la variable de entorno GEMINI_API_KEY en el servidor. "
            "Obtén una clave gratis en https://aistudio.google.com/app/apikey"
        )

    texto = extraer_texto_pdf(datos_pdf)
    system, user = _construir_prompt(texto)

    from google import genai
    from google.genai import types
    from google.genai import errors as genai_errors

    cliente = genai.Client(
        api_key=api_key,
        http_options=types.HttpOptions(timeout=TIMEOUT_IA * 1000),  # ms
    )
    config = types.GenerateContentConfig(
        system_instruction=system,
        temperature=0.2,
        response_mime_type="application/json",
        max_output_tokens=6000,
    )

    # Lista de modelos a probar, sin duplicados y conservando el orden.
    modelos = list(dict.fromkeys(MODELOS_RESPALDO))
    contenido = None
    ultimo_error = None

    for modelo in modelos:
        for intento in range(1, REINTENTOS + 1):
            try:
                respuesta = cliente.models.generate_content(
                    model=modelo, contents=user, config=config
                )
                contenido = respuesta.text
                break
            except genai_errors.ServerError as exc:
                # 503/500: sobrecarga temporal -> esperar y reintentar.
                ultimo_error = exc
                if intento < REINTENTOS:
                    time.sleep(2 * intento)
            except genai_errors.ClientError as exc:
                # 4xx: no tiene sentido reintentar con el mismo modelo.
                ultimo_error = exc
                break
            except Exception as exc:  # noqa: BLE001
                ultimo_error = exc
                break
        if contenido is not None:
            break

    if contenido is None:
        raise ErrorEvaluacion(
            "El servicio de IA está sobrecargado o no respondió. "
            f"Intenta de nuevo en unos segundos. Detalle: {ultimo_error}"
        )

    try:
        resultado = json.loads(_limpiar_json(contenido))
    except json.JSONDecodeError as exc:
        raise ErrorEvaluacion(
            "El modelo devolvió una respuesta que no es JSON válido."
        ) from exc

    return _normalizar(resultado)

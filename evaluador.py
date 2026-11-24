"""Lógica de evaluación: extrae texto del PDF y lo evalúa con Google Gemini."""
import io
import json
import os
import time

import pypdf

from rubrica import ESCALA, rubrica_texto

MAX_CHARS = int(os.environ.get("MAX_PDF_CHARS", "60000"))
TIMEOUT_IA = int(os.environ.get("TIMEOUT_IA", "90"))
REINTENTOS = int(os.environ.get("REINTENTOS_IA", "3"))

# El modelo principal se toma de GEMINI_MODEL; si da 503 (sobrecarga),
# se prueban los siguientes como respaldo.
MODELO_GEMINI = os.environ.get("GEMINI_MODEL", "gemini-3.1-flash-lite")
MODELOS_RESPALDO = [
    MODELO_GEMINI,
    "gemini-3.5-flash-lite",
    "gemini-3.6-flash",
    "gemini-flash-latest",
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
        "resumen_diagnostico": "string (4-6 frases, diagnóstico cualitativo global del diseño, SIN números ni notas)",
        "valoracion_global": "string (etiqueta cualitativa del estado del diseño, p. ej. 'Diseño sólido con vacíos en coherencia' - NUNCA un número)",
        "dimensiones": [
            {
                "id": "string (id exacto de la dimensión de la rúbrica)",
                "nombre": "string",
                "nivel": "string: Cumplido | Parcial | Incipiente | Ausente | No aplica",
                "diagnostico": "string (análisis cualitativo de la dimensión, con evidencia del documento)",
                "criterios": [
                    {
                        "criterio": "string (el criterio evaluado)",
                        "nivel": "string: Cumplido | Parcial | Incipiente | Ausente | No aplica",
                        "hallazgo": "string (respuesta a la pregunta diagnóstica con evidencia textual del documento; cita o parafrasea lo que dice el diseño)",
                    }
                ],
                "fortalezas": ["string"],
                "debilidades": ["string"],
                "recomendaciones": ["string (cambios concretos sobre el diseño)"],
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
        "cambios_prioritarios": ["string (cambios concretos recomendados sobre el diseño del negocio)"],
    }


def _construir_prompt(texto_negocio: str) -> tuple:
    system = (
        "Actúas como evaluador e ingeniero de negocios digitales. Evalúas la "
        "versión preliminar del DISEÑO de un negocio digital (Talleres #1 a #3) "
        "y entregas un DIAGNÓSTICO CUALITATIVO, con rigor técnico y tono "
        "profesional, objetivo y constructivo. Usas únicamente los marcos de la "
        "metodología provista (Modelo de Negocio, Modelo Estratégico, Mapa de "
        "Capacidades, Análisis Estratégico y la cascada de Playing to Win). "
        "REGLA ABSOLUTA: NO asignes calificaciones numéricas, puntajes, notas ni "
        "porcentajes de ningún tipo; el diagnóstico es puramente cualitativo "
        "mediante las etiquetas de nivel definidas. Si el documento no aporta "
        "información para un criterio, dilo explícitamente y usa el nivel "
        "'Ausente' o 'Incipiente'. No inventes datos del negocio que no estén en "
        "el documento; para el análisis competitivo sí puedes citar empresas "
        "reales del mercado."
    )

    user = f"""Diagnostica cualitativamente el siguiente diseño de negocio digital.

=== METODOLOGÍA DE EVALUACIÓN (dimensiones, criterios y su propósito) ===
{rubrica_texto()}

=== NIVELES DE CUMPLIMIENTO (cualitativos, SIN números) ===
{ESCALA}

=== INSTRUCCIONES ===
1. Para cada dimensión, evalúa cada uno de sus criterios asignando un nivel cualitativo y un hallazgo breve con evidencia del documento. Luego da un nivel y un diagnóstico cualitativo de la dimensión completa, con fortalezas, debilidades y recomendaciones de cambio concretas.
2. ANÁLISIS COMPETITIVO: identifica entre 2 y 4 productos o empresas REALES del mercado comparables. Explica qué hacen, en qué se parecen y qué hacen mejor. Determina qué diferencia al negocio, si tiene ventaja competitiva sostenible y su posicionamiento.
3. Da un resumen de diagnóstico global y una valoración global en PALABRAS (nunca un número).
4. Lista riesgos principales y cambios prioritarios concretos sobre el diseño.
5. NO uses puntajes, notas, porcentajes ni escalas numéricas en ninguna parte.
6. Responde ÚNICAMENTE con un JSON válido que cumpla EXACTAMENTE este esquema (sin texto adicional, sin markdown):

{json.dumps(_esquema(), ensure_ascii=False, indent=2)}

=== DOCUMENTO (DISEÑO DEL NEGOCIO DIGITAL - TALLER #3) ===
{texto_negocio}
"""
    return system, user


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
        max_output_tokens=8192,
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

    return resultado

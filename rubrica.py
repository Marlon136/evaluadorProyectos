"""
Rúbrica de evaluación de negocios digitales.

Los criterios se derivan de las lecturas del curso de Arquitectura de Negocio:
  - El Modelo de Negocio (Lectura #2): portafolio de servicios, estructura
    (actores, canales), modelo ontológico, propuesta/promesa de valor,
    journeys del cliente.
  - El Modelo Estratégico: componente motivacional (propósito superior,
    objetivo retador, visión, misión, valores), promesa de valor y
    componente de objetivos (objetivos, metas, indicadores de logro).
  - El Mapa de Capacidades: capacidades de negocio (acción con verbo activo)
    y su implementación/madurez.
  - Análisis Estratégico Empresarial: DOFA, 5 fuerzas de Porter, PEST, BCG,
    McKinsey, análisis de clientes, financiero, de TI y de riesgos.
  - Playing to Win (Lafley & Martin): la cascada de 5 decisiones estratégicas
    (aspiración ganadora, dónde competir, cómo ganar, capacidades, sistemas
    de gestión).
"""

# Cada dimensión tiene un peso (suma 100). Los criterios guían al evaluador.
DIMENSIONES = [
    {
        "id": "modelo_negocio",
        "nombre": "Modelo de negocio",
        "peso": 20,
        "fuente": "Lectura #2 - El Modelo de Negocio",
        "criterios": [
            "El portafolio de servicios está claramente definido (qué hace el negocio como caja negra).",
            "La estructura de negocio identifica actores (clientes, usuarios, proveedores, socios) y canales.",
            "Se distingue con claridad entre cliente (quien paga) y usuario (quien recibe el valor).",
            "El objeto de negocio / tipo de valor que se entrega es explícito (producto físico o digital, servicio, plataforma, dinero, etc.).",
            "El mecanismo de monetización está definido (cómo el valor se intercambia por dinero).",
        ],
    },
    {
        "id": "propuesta_valor",
        "nombre": "Propuesta / promesa de valor",
        "peso": 18,
        "fuente": "Lectura #2 y El Modelo Estratégico",
        "criterios": [
            "La propuesta de valor es clara, específica y diferenciadora frente a competidores.",
            "Resuelve un problema o necesidad real y relevante de un segmento de clientes bien definido.",
            "Se evidencia por qué un cliente elegiría este negocio sobre las alternativas.",
            "Hay coherencia entre la promesa de valor y los servicios ofrecidos.",
        ],
    },
    {
        "id": "estrategia",
        "nombre": "Modelo estratégico y cascada de decisiones",
        "peso": 20,
        "fuente": "El Modelo Estratégico + Playing to Win (Lafley & Martin)",
        "criterios": [
            "Componente motivacional presente: propósito superior, objetivo retador, visión, misión y valores.",
            "Aspiración ganadora: existe una definición clara de qué significa ganar.",
            "Dónde competir: mercados, segmentos, geografías y canales están delimitados.",
            "Cómo ganar: la lógica de ventaja competitiva es explícita (costo, diferenciación, nicho).",
            "Coherencia interna de la cascada: las decisiones se refuerzan entre sí.",
        ],
    },
    {
        "id": "capacidades",
        "nombre": "Capacidades de negocio",
        "peso": 12,
        "fuente": "Lectura #1 - El Mapa de Capacidades",
        "criterios": [
            "Las capacidades clave del negocio están identificadas y expresadas como acciones (verbo activo), no como objetivos.",
            "Las capacidades se derivan de y soportan la intención del negocio.",
            "Se evidencian las capacidades distintivas que habilitan la ventaja competitiva.",
            "Hay una noción de cómo se implementan (personas, procesos, recursos/tecnología).",
        ],
    },
    {
        "id": "clientes_mercado",
        "nombre": "Clientes, mercado y entorno competitivo",
        "peso": 15,
        "fuente": "Análisis Estratégico Empresarial (Porter, PEST, clientes)",
        "criterios": [
            "Segmentación de clientes clara y conocimiento de sus necesidades (journeys).",
            "Análisis del entorno competitivo (5 fuerzas de Porter: rivalidad, entrantes, sustitutos, poder de proveedores y clientes).",
            "Consideración del entorno macro (PEST: político, económico, social, tecnológico).",
            "Tamaño de mercado y potencial de crecimiento razonados.",
        ],
    },
    {
        "id": "viabilidad",
        "nombre": "Viabilidad financiera y operativa",
        "peso": 15,
        "fuente": "Análisis Estratégico Empresarial (financiero, TI, riesgos)",
        "criterios": [
            "Modelo de ingresos y estructura de costos coherentes y sostenibles.",
            "Indicadores y metas definidos (modelo de indicadores: objetivos, metas, indicadores de logro).",
            "Viabilidad del componente de TI / plataforma digital que soporta el negocio.",
            "Identificación de hallazgos y riesgos principales, con mitigaciones.",
        ],
    },
]

ESCALA = (
    "Escala de calificación por dimensión (0 a 5):\n"
    "  5 - Excelente: cumple de forma sobresaliente y diferenciada.\n"
    "  4 - Bueno: cumple sólidamente con oportunidades menores de mejora.\n"
    "  3 - Aceptable: cumple lo básico pero con vacíos relevantes.\n"
    "  2 - Débil: cumplimiento parcial, con vacíos importantes.\n"
    "  1 - Muy débil: apenas abordado o incoherente.\n"
    "  0 - Ausente: no se aborda en el documento."
)


def rubrica_texto() -> str:
    """Devuelve la rúbrica formateada para inyectar en el prompt del LLM."""
    bloques = []
    for d in DIMENSIONES:
        criterios = "\n".join(f"      - {c}" for c in d["criterios"])
        bloques.append(
            f"  Dimensión: {d['nombre']} (id={d['id']}, peso={d['peso']}%)\n"
            f"    Fuente: {d['fuente']}\n"
            f"    Criterios:\n{criterios}"
        )
    return "\n\n".join(bloques)

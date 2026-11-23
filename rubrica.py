"""
Metodología de evaluación cualitativa de un negocio digital.

Ejercicio ISIS-2411 (Reemplazo Examen #2). El asistente evalúa la versión
preliminar del diseño del negocio digital (Talleres #1 a #3) y entrega un
DIAGNÓSTICO CUALITATIVO, sin calificación numérica (regla c del enunciado).

Los criterios son propios y se apoyan en lo aprendido en el curso (NO en la
rúbrica oficial de los talleres, regla a). La base conceptual proviene de las
lecturas de Arquitectura de Negocio:
  - El Modelo de Negocio: portafolio de servicios, estructura (actores,
    canales), modelo ontológico, propuesta/promesa de valor, journeys.
  - El Modelo Estratégico: componente motivacional (propósito superior,
    objetivo retador, visión, misión, valores), promesa de valor y
    componente de objetivos (objetivos, metas, indicadores de logro).
  - El Mapa de Capacidades: capacidades de negocio (acción con verbo activo)
    y su implementación.
  - Análisis Estratégico Empresarial: DOFA, 5 fuerzas de Porter, PEST, BCG,
    McKinsey, análisis de clientes, financiero, de TI y de riesgos.
  - Playing to Win (Lafley & Martin): la cascada de decisiones estratégicas
    (aspiración ganadora, dónde competir, cómo ganar, capacidades, sistemas
    de gestión).

La arquitectura de negocio se compone de modelos que deben derivarse unos de
otros y ser coherentes entre sí:
  1. Modelo de intención = modelo de negocio + modelo financiero + modelo
     estratégico.
  2. Modelo de capacidades: se deriva del modelo de intención.
  3. Modelo operativo = organizacional + procesos + recursos.
  4. Modelo de indicadores: mide el logro de los objetivos estratégicos.
  5. Operación: la materialización del modelo operativo.

Cada DIMENSIÓN agrupa criterios afines. Cada CRITERIO tiene:
  - "criterio": qué se revisa.
  - "proposito": qué se quiere verificar y por qué importa en un negocio digital.
"""

DIMENSIONES = [
    {
        "id": "modelo_negocio",
        "nombre": "Modelo de negocio",
        "fuente": "El Modelo de Negocio (Lectura #2)",
        "proposito_dimension": (
            "Verificar que el diseño explica con claridad cómo el negocio "
            "produce valor y lo monetiza. Sin un modelo de negocio explícito, "
            "el resto del diseño carece de fundamento."
        ),
        "criterios": [
            {
                "criterio": "El portafolio de servicios está definido (qué hace el negocio visto como caja negra).",
                "proposito": "Verificar que el negocio sabe qué ofrece; si los servicios no son claros, no se puede diseñar nada aguas abajo.",
            },
            {
                "criterio": "La estructura de negocio identifica actores (clientes, usuarios, proveedores, socios) y canales.",
                "proposito": "Confirmar que se entiende con quién interactúa el negocio y por dónde fluye el valor, base de toda la operación.",
            },
            {
                "criterio": "Se distingue entre cliente (quien paga) y usuario (quien recibe el valor).",
                "proposito": "Evitar un error común en negocios digitales (p. ej. plataformas donde pagador y usuario son distintos) que distorsiona la monetización.",
            },
            {
                "criterio": "El objeto de negocio / tipo de valor es explícito (producto digital, servicio, plataforma, dinero, etc.).",
                "proposito": "Asegurar que se nombró la naturaleza del valor entregado, pues determina el modelo de ingresos y las capacidades necesarias.",
            },
            {
                "criterio": "El mecanismo de monetización está definido (cómo el valor se intercambia por dinero).",
                "proposito": "Comprobar que el negocio es económicamente viable y no solo una idea sin forma de capturar valor.",
            },
        ],
    },
    {
        "id": "propuesta_valor",
        "nombre": "Propuesta / promesa de valor",
        "fuente": "El Modelo de Negocio y El Modelo Estratégico",
        "proposito_dimension": (
            "Verificar que existe una razón convincente por la que un cliente "
            "elegiría este negocio, que es lo que lo hace competitivo."
        ),
        "criterios": [
            {
                "criterio": "La propuesta de valor es clara, específica y diferenciadora frente a competidores.",
                "proposito": "Comprobar que el negocio no es indiferenciado; en lo digital, sin diferenciación la competencia es solo por precio.",
            },
            {
                "criterio": "Resuelve un problema o necesidad real de un segmento de clientes bien definido.",
                "proposito": "Verificar que hay un problema que vale la pena resolver y un cliente dispuesto a pagar por ello.",
            },
            {
                "criterio": "Se evidencia por qué un cliente elegiría este negocio sobre las alternativas.",
                "proposito": "Asegurar que la diferenciación es percibida por el cliente, no solo declarada por el equipo.",
            },
            {
                "criterio": "Hay coherencia entre la promesa de valor y los servicios ofrecidos.",
                "proposito": "Detectar promesas que el portafolio de servicios no puede cumplir, lo que erosiona la confianza del cliente.",
            },
        ],
    },
    {
        "id": "estrategia",
        "nombre": "Modelo estratégico y cascada de decisiones",
        "fuente": "El Modelo Estratégico + Playing to Win (Lafley & Martin)",
        "proposito_dimension": (
            "Verificar que el negocio tiene una dirección estratégica "
            "coherente y no solo un producto, para sostenerse en el tiempo."
        ),
        "criterios": [
            {
                "criterio": "Componente motivacional presente: propósito superior, objetivo retador, visión, misión y valores.",
                "proposito": "Confirmar que hay un norte que alinea decisiones y equipo; sin él, el negocio reacciona sin rumbo.",
            },
            {
                "criterio": "Aspiración ganadora: hay una definición clara de qué significa ganar.",
                "proposito": "Verificar que el equipo sabe a qué aspira; sin meta de éxito no se puede medir el avance ni priorizar.",
            },
            {
                "criterio": "Dónde competir: mercados, segmentos, geografías y canales están delimitados.",
                "proposito": "Comprobar que el negocio eligió un terreno de juego; querer competir en todo suele llevar a no ganar en nada.",
            },
            {
                "criterio": "Cómo ganar: la lógica de ventaja competitiva es explícita (costo, diferenciación o nicho).",
                "proposito": "Asegurar que hay una teoría de cómo vencer a los rivales, no solo intención de participar.",
            },
            {
                "criterio": "Coherencia interna de la cascada: las decisiones estratégicas se refuerzan entre sí.",
                "proposito": "Detectar contradicciones (p. ej. aspirar a liderazgo en costos y a la vez a máxima personalización) que debilitan la estrategia.",
            },
        ],
    },
    {
        "id": "capacidades",
        "nombre": "Capacidades de negocio",
        "fuente": "El Mapa de Capacidades (Lectura #1)",
        "proposito_dimension": (
            "Verificar que el diseño identifica qué debe saber hacer el "
            "negocio para cumplir su intención, el puente entre estrategia y "
            "operación."
        ),
        "criterios": [
            {
                "criterio": "Las capacidades clave están identificadas y expresadas como acciones (verbo activo), no como objetivos.",
                "proposito": "Comprobar que se entiende qué es una capacidad; confundirlas con objetivos impide luego diseñar la operación.",
            },
            {
                "criterio": "Las capacidades se derivan de y soportan la intención del negocio.",
                "proposito": "Verificar la trazabilidad estrategia→capacidades; capacidades sueltas indican diseño desarticulado.",
            },
            {
                "criterio": "Se evidencian las capacidades distintivas que habilitan la ventaja competitiva.",
                "proposito": "Asegurar que el negocio sabe cuáles capacidades lo hacen ganar y cuáles son solo de soporte.",
            },
            {
                "criterio": "Hay una noción de cómo se implementan (personas, procesos, recursos/tecnología).",
                "proposito": "Confirmar que las capacidades son realizables y no abstracciones sin plan de ejecución.",
            },
        ],
    },
    {
        "id": "clientes_mercado",
        "nombre": "Clientes, mercado y entorno competitivo",
        "fuente": "Análisis Estratégico Empresarial (Porter, PEST, clientes)",
        "proposito_dimension": (
            "Verificar que el diseño mira hacia afuera: entiende a sus "
            "clientes y el entorno donde compite, no solo el producto."
        ),
        "criterios": [
            {
                "criterio": "Segmentación de clientes clara y conocimiento de sus necesidades (journeys).",
                "proposito": "Comprobar que el negocio conoce a quién sirve; un segmento difuso lleva a producto y marketing difusos.",
            },
            {
                "criterio": "Análisis del entorno competitivo (5 fuerzas de Porter).",
                "proposito": "Verificar que se evaluó la presión competitiva (rivales, entrantes, sustitutos, poder de proveedores y clientes).",
            },
            {
                "criterio": "Consideración del entorno macro (PEST: político, económico, social, tecnológico).",
                "proposito": "Asegurar que se anticiparon factores externos que pueden habilitar o amenazar al negocio digital.",
            },
            {
                "criterio": "Tamaño de mercado y potencial de crecimiento razonados.",
                "proposito": "Confirmar que la oportunidad justifica el esfuerzo; un mercado demasiado pequeño limita la viabilidad.",
            },
        ],
    },
    {
        "id": "viabilidad",
        "nombre": "Viabilidad financiera y operativa",
        "fuente": "Análisis Estratégico Empresarial (financiero, TI, riesgos)",
        "proposito_dimension": (
            "Verificar que el negocio puede sostenerse económica y "
            "operativamente, y que reconoce sus riesgos."
        ),
        "criterios": [
            {
                "criterio": "Modelo de ingresos y estructura de costos coherentes y sostenibles.",
                "proposito": "Comprobar que el negocio puede ganar más de lo que gasta; la base de cualquier sostenibilidad.",
            },
            {
                "criterio": "Indicadores y metas definidos (objetivos, metas, indicadores de logro).",
                "proposito": "Verificar que el negocio sabe cómo medirá su éxito; sin indicadores no hay gestión posible.",
            },
            {
                "criterio": "Viabilidad del componente de TI / plataforma digital que soporta el negocio.",
                "proposito": "Asegurar que la tecnología que habilita el negocio digital es factible y adecuada al modelo.",
            },
            {
                "criterio": "Identificación de hallazgos y riesgos principales, con mitigaciones.",
                "proposito": "Confirmar que el equipo anticipa qué puede salir mal y cómo responder, señal de madurez del diseño.",
            },
        ],
    },
    {
        "id": "modelos_arquitectura",
        "nombre": "Completitud y coherencia de los modelos del negocio",
        "fuente": "El Mapa de Capacidades (arquitectura de negocio) + Modelos y Metamodelos",
        "proposito_dimension": (
            "Verificar que el diseño define los modelos que un negocio digital "
            "debe tener y que son coherentes entre sí (se derivan unos de "
            "otros), que es lo central de la Arquitectura de Negocio del curso."
        ),
        "criterios": [
            {
                "criterio": "El documento DEFINE los modelos que un negocio digital debe tener, no solo ideas sueltas.",
                "proposito": "Comprobar que el diseño es una arquitectura estructurada y no una colección de notas inconexas.",
            },
            {
                "criterio": "Modelo de intención presente: modelo de negocio, modelo financiero y modelo estratégico.",
                "proposito": "Verificar que está definido qué pretende lograr el negocio, punto de partida de toda la arquitectura.",
            },
            {
                "criterio": "Modelo de capacidades presente y DERIVADO de la intención.",
                "proposito": "Asegurar trazabilidad: las capacidades responden a lo que el negocio quiere lograr, no aparecen de la nada.",
            },
            {
                "criterio": "Modelo operativo esbozado (organización, procesos y recursos/tecnología) que implementa las capacidades.",
                "proposito": "Confirmar que hay un puente del qué al cómo; capacidades sin operación quedan como intenciones.",
            },
            {
                "criterio": "Modelo de indicadores presente y alineado con los objetivos estratégicos.",
                "proposito": "Verificar que lo que se mide corresponde a lo que se quiere lograr, cerrando el ciclo de gestión.",
            },
            {
                "criterio": "COHERENCIA entre modelos: cada modelo se deriva del anterior y no hay contradicciones.",
                "proposito": "Detectar desconexiones (estrategia que no se refleja en capacidades, u operación que no las implementa) que invalidan el diseño.",
            },
            {
                "criterio": "La plataforma digital (TI) es coherente con el modelo de negocio y las capacidades que debe habilitar.",
                "proposito": "Asegurar que la tecnología sirve al negocio y no al revés, clave en un negocio digital.",
            },
        ],
    },
]

# Diagnóstico CUALITATIVO por criterio y por dimensión (sin números).
NIVELES = [
    "Cumplido",
    "Parcial",
    "Incipiente",
    "Ausente",
    "No aplica",
]

ESCALA = (
    "Nivel de cumplimiento CUALITATIVO (sin puntajes numéricos). "
    "Usa exactamente una de estas etiquetas por criterio y por dimensión:\n"
    "  - Cumplido: el diseño aborda el criterio de forma clara y sólida.\n"
    "  - Parcial: lo aborda, pero con vacíos relevantes o poca profundidad.\n"
    "  - Incipiente: apenas se insinúa; falta desarrollo sustancial.\n"
    "  - Ausente: el diseño no aborda el criterio.\n"
    "  - No aplica: el criterio no es pertinente para este negocio (justifícalo)."
)


def rubrica_texto() -> str:
    """Devuelve la metodología formateada para inyectar en el prompt del LLM."""
    bloques = []
    for d in DIMENSIONES:
        criterios = "\n".join(
            f"      - Criterio: {c['criterio']}\n"
            f"        Propósito: {c['proposito']}"
            for c in d["criterios"]
        )
        bloques.append(
            f"  Dimensión: {d['nombre']} (id={d['id']})\n"
            f"    Fuente: {d['fuente']}\n"
            f"    Propósito de la dimensión: {d['proposito_dimension']}\n"
            f"    Criterios:\n{criterios}"
        )
    return "\n\n".join(bloques)

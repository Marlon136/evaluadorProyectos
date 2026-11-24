"""
Metodología de evaluación cualitativa del diseño de un negocio digital.

Ejercicio ISIS-2411 (Reemplazo Examen #2). El asistente evalúa la versión
preliminar del diseño del negocio digital (Talleres #1 a #3) y entrega un
DIAGNÓSTICO CUALITATIVO, sin calificación numérica (regla c del enunciado).

Los criterios son propios. Se construyeron a partir de tres fuentes de nuestro
propio trabajo:
  1. Las correcciones puntuales que el profesor nos hizo sobre el diseño.
  2. Nuestras notas de clase (vocabulario y definiciones textuales del curso).
  3. Las lecturas de Arquitectura de Negocio y Playing to Win.
NO se usó la rúbrica oficial de los talleres (regla a).

El diagnóstico es CUALITATIVO y conceptual: evalúa si cada elemento del diseño
está BIEN DEFINIDO según el curso, no si hay cierta cantidad de elementos.

Vocabulario del curso usado en los criterios (según nuestras notas):
  - Negocio digital: genera utilidades y resuelve problemas; lo digital está en
    estar en línea, en tiempo real y sin barreras geográficas.
  - Un negocio digital se representa con 4 dominios: Negocio, Información,
    Aplicaciones y TI.
  - Servicio de negocio: una ACCIÓN que genera valor y monetiza (los tres
    checks). No toda acción es servicio. El resultado y la forma de adquirirlo
    NO hacen parte del servicio.
  - Objeto de negocio (el valor entregado): puede ser Resultado, Servicio,
    Información, Dinero o Plataforma. Producto entrega un objeto de forma
    indefinida; bien lo entrega temporalmente.
  - Actores: cliente (paga), usuario (usa pero no paga), prospecto/potencial,
    temporal.
  - Línea de negocio: organiza y agrupa servicios.
  - Estructura de negocio: componentes que participan en crear/entregar valor,
    conectados por canales por donde fluyen información y dinero.
  - Canales: directos (conectan el negocio con otro componente) e indirectos
    (sobre los que no se tiene control). Lo que distingue dos canales del mismo
    tipo: distintas actividades, distintos recursos/medios.
  - Recursos: entidad del metamodelo, responden CON QUÉ se ejecutan las
    actividades. Medios: no son entidad, responden POR DÓNDE ocurre la
    interacción del canal.
  - Escenario de negocio: diagrama que cuenta una historia mostrando el ORDEN
    (línea de tiempo) de las actividades de los canales y componentes externos.
  - Flujo de valor: secuencia de CAPACIDADES que permiten entregar un servicio.
  - Capacidad de negocio: lo que la empresa puede y sabe hacer; atemporal, sin
    indicador de logro; se expresa como acción (verbo activo). Capacidad crítica:
    la que se reusa entre flujos de valor y/o genera el diferencial.
  - Mapa de capacidades: no tiene capacidades duplicadas; capacidades únicas con
    único dueño; se agrupan por lo que facilitan (funcional, misional,
    estratégico).
  - Metamodelo de negocio / modelo ontológico: modelo de DOMINIO; NO incluye
    infraestructura ni TI (no web, BD, nube, pasarelas), NO inmuebles, NO
    estructura organizacional.
  - Frontera digital: interconecta las actividades/interacciones digitales con
    las físicas. Al volverse digital, la comunicación entre actores (conexión,
    relacionamiento, orquestación) se vuelve el principal productor de valor.
  - Trazabilidad: la ingeniería de negocio sirve para saber tomar decisiones;
    un cambio en un modelo debe poder rastrearse en los demás.

Cada CRITERIO tiene:
  - "criterio": qué se revisa, con el vocabulario del curso.
  - "pregunta": la pregunta diagnóstica concreta que el asistente responde
    leyendo el documento.
  - "proposito": qué se verifica y la consecuencia de no cumplirlo.
"""

DIMENSIONES = [
    # ------------------------------------------------------------------
    {
        "id": "servicios",
        "nombre": "Servicios de negocio y objeto de valor",
        "fuente": "Notas de clase (definición de servicio) + El Modelo de Negocio",
        "proposito_dimension": (
            "Verificar que los servicios están bien definidos según el curso: "
            "una acción que genera valor y monetiza. Es la base del modelo "
            "funcional; un servicio mal definido arrastra errores a todo el diseño."
        ),
        "criterios": [
            {
                "criterio": "Cada servicio de negocio es una ACCIÓN que genera valor y que monetiza (los tres a la vez).",
                "pregunta": "¿Cada servicio cumple los tres checks: es una acción, genera valor y monetiza? ¿Hay 'servicios' que en realidad no monetizan o no son acción?",
                "proposito": "Es la definición exacta del curso ('no toda acción es servicio de negocio: debe cumplir acción, genera valor, monetización'). Un servicio que no monetiza no es servicio y distorsiona el portafolio.",
            },
            {
                "criterio": "El servicio se redacta con un verbo de acción adecuado (p. ej. 'vender', no 'crear') y no mezcla el resultado ni la forma de adquirirlo.",
                "pregunta": "¿El verbo del servicio es correcto y el servicio no incluye el resultado ni cómo se adquiere?",
                "proposito": "El profesor marcó errores de portafolio por el verbo ('crear' en vez de 'vender') y porque 'el resultado NO hace parte del servicio, tampoco cómo lo adquiere'.",
            },
            {
                "criterio": "El objeto de negocio de cada servicio está tipificado (Resultado, Servicio, Información, Dinero o Plataforma).",
                "pregunta": "¿Se dice qué objeto de negocio entrega cada servicio y de qué tipo es?",
                "proposito": "El objeto de negocio es el valor que recibe el actor; sin tipificarlo no se sabe qué se está entregando ni cómo se monetiza.",
            },
            {
                "criterio": "Los servicios se agrupan en líneas de negocio coherentes.",
                "pregunta": "¿El portafolio está organizado en líneas de negocio que agrupan servicios afines?",
                "proposito": "Según las notas, 'la línea de negocio organiza y agrupa servicios'. Un portafolio plano sin líneas no refleja cómo está estructurado el negocio.",
            },
        ],
    },
    # ------------------------------------------------------------------
    {
        "id": "estructura_actores_canales",
        "nombre": "Estructura de negocio: actores y canales",
        "fuente": "Notas de clase (actores, canales, recursos/medios) + El Modelo de Negocio",
        "proposito_dimension": (
            "Verificar que la estructura de negocio identifica bien los actores y "
            "los canales por donde fluye el valor, con la precisión de vocabulario "
            "del curso."
        ),
        "criterios": [
            {
                "criterio": "Los actores están bien clasificados: cliente (paga), usuario (usa pero no paga), y cuando aplique prospecto/potencial o temporal.",
                "pregunta": "¿Se distingue quién paga (cliente) de quién recibe el valor (usuario), y se usan prospecto/temporal donde corresponda?",
                "proposito": "El curso define estos tipos de actor; confundir cliente con usuario (error que el profesor señala) distorsiona la monetización y el diseño de canales.",
            },
            {
                "criterio": "Los canales están identificados y clasificados como directos (conectan el negocio con un componente) o indirectos (sobre los que no se tiene control).",
                "pregunta": "¿Los canales se nombran y se dice si son directos o indirectos?",
                "proposito": "Es la tipología de canales del curso; un canal indirecto implica pérdida de control que debe quedar explícita.",
            },
            {
                "criterio": "Para canales del mismo tipo, se distingue qué los diferencia (distintas actividades, distintos recursos o medios).",
                "pregunta": "¿Cuando hay varios canales del mismo tipo, se explica qué los hace distintos (actividades/recursos/medios)?",
                "proposito": "El curso pregunta '¿qué distingue dos canales de un mismo tipo?'. Sin esa distinción, los canales son indistinguibles y el modelo pierde precisión.",
            },
            {
                "criterio": "Se distinguen recursos (CON QUÉ se ejecutan las actividades, son entidad) de medios (POR DÓNDE ocurre la interacción, no son entidad).",
                "pregunta": "¿El diseño diferencia recursos de medios según la definición del curso?",
                "proposito": "Las notas lo marcan explícitamente; confundirlos lleva a modelar como entidad algo que no lo es.",
            },
            {
                "criterio": "Se muestran las actividades por tipo de canal (aprovisionamiento, transformación, distribución, monetización, relacionamiento).",
                "pregunta": "¿Cada canal tiene actividades asociadas coherentes con su tipo?",
                "proposito": "Es el marco de actividades por canal del curso; un canal sin actividades no explica cómo participa en crear o entregar valor.",
            },
        ],
    },
    # ------------------------------------------------------------------
    {
        "id": "escenarios",
        "nombre": "Escenarios de negocio",
        "fuente": "Notas de clase (definición de escenario) + correcciones del profesor",
        "proposito_dimension": (
            "Verificar que los escenarios cuentan bien la historia dinámica del "
            "negocio (el orden de las actividades) y muestran dónde se genera el "
            "diferencial, como pidió el profesor."
        ),
        "criterios": [
            {
                "criterio": "Cada escenario cuenta una historia mostrando el ORDEN (línea de tiempo) de las actividades de los canales y las acciones de los componentes externos.",
                "pregunta": "¿Los escenarios muestran la secuencia temporal de actividades y no solo una lista estática?",
                "proposito": "Es la definición del curso de escenario de negocio; sin el orden temporal no es un escenario, es una enumeración.",
            },
            {
                "criterio": "Los escenarios distinguen flujos de valor distintos (p. ej. venta, entrega, pago) cuando corresponde.",
                "pregunta": "¿Se separan los distintos flujos de valor dentro de los escenarios en lugar de mezclarlos?",
                "proposito": "El profesor señaló que 'por servicio hay varios flujos de valor (venta, entrega, pago)'. Mezclarlos oculta pasos de entrega de valor.",
            },
            {
                "criterio": "Se identifica el escenario que más impacta y se explica qué cambia en la experiencia del actor (dónde está el diferencial).",
                "pregunta": "¿Se señala el escenario de mayor impacto y qué cambia en la experiencia para generar diferencial?",
                "proposito": "El profesor pidió 'representar el escenario que más impacta' y 'mostrar qué cambia la experiencia'. Es lo que separa un escenario descriptivo de uno estratégico.",
            },
        ],
    },
    # ------------------------------------------------------------------
    {
        "id": "capacidades",
        "nombre": "Capacidades, flujos de valor y capacidad crítica",
        "fuente": "Notas de clase (capacidad, flujo de valor) + El Mapa de Capacidades + correcciones",
        "proposito_dimension": (
            "Verificar que las capacidades y los flujos de valor están bien "
            "entendidos según el curso, y que se identifica y justifica la "
            "capacidad crítica que genera el diferencial."
        ),
        "criterios": [
            {
                "criterio": "Las capacidades se expresan como acción (lo que la empresa puede y sabe hacer), son atemporales y no se confunden con objetivos ni indicadores de logro.",
                "pregunta": "¿Las capacidades están redactadas como acciones y no como metas u objetivos con indicador?",
                "proposito": "Las notas definen capacidad como 'lo que la empresa puede y sabe hacer, atemporal, sin indicador de logro'. Una capacidad mal redactada no se puede implementar.",
            },
            {
                "criterio": "Los flujos de valor están definidos como una secuencia de capacidades que permite entregar un servicio.",
                "pregunta": "¿Cada flujo de valor se describe como una secuencia de capacidades que entrega un servicio?",
                "proposito": "Definición textual del curso ('flujo de valor = secuencia de capacidades que permiten entregar un servicio'). Si no se liga a capacidades, no es un flujo de valor.",
            },
            {
                "criterio": "Se identifica la capacidad crítica (la que se reusa entre flujos de valor y/o genera el diferencial) y se justifica por sus actividades y recursos.",
                "pregunta": "¿Se señala la capacidad crítica, se dice por qué es crítica y qué diferencial genera, con base en sus actividades y recursos?",
                "proposito": "El profesor pidió 'al menos una capacidad crítica que genere diferencial' y justificarla 'desde las actividades y recursos'. Las notas añaden que es 'la que se reusa entre flujos'.",
            },
            {
                "criterio": "Cada capacidad tiene recursos asociados explícitos y se indica qué actividades cubre.",
                "pregunta": "¿Cada capacidad lista sus recursos y las actividades que cubre?",
                "proposito": "El profesor pidió 'hacer explícitos los recursos asociados a cada capacidad' y 'qué actividades cubre'. Sin esto la capacidad no es implementable.",
            },
            {
                "criterio": "El mapa de capacidades no tiene capacidades duplicadas: son únicas, con único dueño, agrupadas por lo que facilitan (funcional, misional, estratégico).",
                "pregunta": "¿Las capacidades son únicas (sin duplicados) y están agrupadas por tipo (funcional/misional/estratégico)?",
                "proposito": "Las notas lo marcan: 'el mapa NO puede tener capacidades duplicadas, capacidades únicas con único dueño'. Duplicados indican que no se entendió el modelo.",
            },
        ],
    },
    # ------------------------------------------------------------------
    {
        "id": "modelo_operativo",
        "nombre": "Modelo operativo: procesos y procedimientos",
        "fuente": "Correcciones del profesor + El Modelo Operativo",
        "proposito_dimension": (
            "Verificar que el modelo operativo representa cómo se implementa el "
            "servicio conectando flujos de valor, servicios, capacidades y "
            "procesos, respetando las reglas de modelado del profesor."
        ),
        "criterios": [
            {
                "criterio": "El modelo operativo es un flujo lógico que conecta flujos de valor, servicios de negocio y capacidades (no es un listado de tareas).",
                "pregunta": "¿El modelo operativo conecta flujos de valor, servicios y capacidades como un flujo lógico?",
                "proposito": "El profesor definió el modelo operativo así; si no conecta esos elementos pierde su función de puente entre intención y operación.",
            },
            {
                "criterio": "Se distingue proceso (el QUÉ, medible y cuantificable, orquesta personas/áreas/tecnologías) de procedimiento (el CÓMO se genera y entrega valor).",
                "pregunta": "¿El diseño diferencia procesos de procedimientos según la definición del curso?",
                "proposito": "El profesor marcó esta distinción; confundirlos impide medir la operación.",
            },
            {
                "criterio": "Se especifica qué procesos apoyan cada servicio y qué procesos participan en más de un flujo de valor.",
                "pregunta": "¿Se dice qué procesos soportan cada servicio y cuáles aparecen en varios flujos de valor?",
                "proposito": "El profesor preguntó '¿cuáles procesos participan en más de un flujo de valor?' y pidió dejar explícito qué procesos apoyan cada servicio.",
            },
            {
                "criterio": "En las vistas de ArchiMate solo se representa el nombre del proceso, sin modelar sus actividades internas.",
                "pregunta": "¿Las vistas evitan modelar el detalle interno de procesos/procedimientos (solo el nombre del proceso)?",
                "proposito": "Regla explícita del profesor: 'en las vistas de Archi nunca se representan las actividades de los procesos'.",
            },
        ],
    },
    # ------------------------------------------------------------------
    {
        "id": "arquitectura_ti",
        "nombre": "Aplicaciones y tecnología (dominios de información, aplicaciones y TI)",
        "fuente": "Notas de clase (4 dominios, frontera digital) + correcciones del profesor",
        "proposito_dimension": (
            "Verificar que la capa de información/aplicaciones/TI define dueño de "
            "la información y comunicación entre aplicaciones, y cumple las "
            "exigencias no negociables del profesor (escalabilidad, bajo "
            "acoplamiento, bus)."
        ),
        "criterios": [
            {
                "criterio": "Está definido qué aplicación es dueña de qué información.",
                "pregunta": "¿Se identifica, por aplicación, de qué información es dueña?",
                "proposito": "El profesor lo llamó 'vista importante: ¿qué app es dueña de qué información?'. Sin dueño de la información hay inconsistencias y duplicación.",
            },
            {
                "criterio": "Las aplicaciones se derivan de requerimientos y se define cómo se comunican (flujo de información).",
                "pregunta": "¿Se derivan las aplicaciones de requerimientos y se define el flujo de información entre ellas?",
                "proposito": "El profesor pidió la secuencia 'requerimientos → cuáles aplicaciones → cómo se comunican'.",
            },
            {
                "criterio": "La tecnología cumple escalabilidad y bajo acoplamiento (requisito no negociable).",
                "pregunta": "¿El diseño argumenta que la solución puede escalar fácilmente y tiene bajo acoplamiento?",
                "proposito": "El profesor dijo que la tecnología 'tiene que cumplir sí o sí escalar y bajo acoplamiento'. Es eliminatorio para él.",
            },
            {
                "criterio": "Existe un componente que habilita la comunicación entre aplicaciones (bus) con mediadores/adaptadores, y las aplicaciones son lo más atómicas posible.",
                "pregunta": "¿Hay un bus de integración con adaptadores/mediadores y las aplicaciones son atómicas para facilitar la orquestación?",
                "proposito": "El profesor recomendó el bus, los mediadores y aplicaciones atómicas 'para facilitar la orquestación'.",
            },
            {
                "criterio": "El metamodelo de negocio no mezcla TI ni infraestructura (respeta la separación de dominios).",
                "pregunta": "¿El modelo de dominio/ontológico se mantiene sin infraestructura, TI específica, inmuebles ni estructura organizacional?",
                "proposito": "Las notas son explícitas: el metamodelo de negocio 'NO incluye infraestructura ni TI'. Mezclar dominios revela que no se entendió la separación.",
            },
        ],
    },
    # ------------------------------------------------------------------
    {
        "id": "modelo_estrategico",
        "nombre": "Modelo estratégico y prioridad",
        "fuente": "El Modelo Estratégico + Playing to Win + correcciones del profesor",
        "proposito_dimension": (
            "Verificar que la estrategia está bien definida sobre los dominios del "
            "negocio, con una prioridad clara y una lógica de cómo ganar coherente."
        ),
        "criterios": [
            {
                "criterio": "Está declarada la prioridad estratégica del negocio.",
                "pregunta": "¿El documento dice explícitamente cuál es la prioridad estratégica?",
                "proposito": "El profesor pidió 'saber cuál es la prioridad estratégica'. Sin prioridad no se puede decidir en qué invertir primero (y las notas la ligan al grupo de capacidades con prioridad de inversión).",
            },
            {
                "criterio": "La estrategia se sustenta mirando los dominios del negocio y no una idea aislada.",
                "pregunta": "¿La definición estratégica se apoya en los dominios del negocio y en su estructura?",
                "proposito": "El profesor dijo que para la estrategia 'hay que evaluar los dominios'. Una estrategia que ignora dominios ignora restricciones reales.",
            },
            {
                "criterio": "Cómo ganar: la lógica de ventaja competitiva es explícita y coherente con dónde se decidió competir (Playing to Win).",
                "pregunta": "¿Se explicita cómo gana el negocio y es coherente con su terreno de juego?",
                "proposito": "Núcleo de Playing to Win; sin un 'cómo ganar' la estrategia es solo participar.",
            },
            {
                "criterio": "El componente motivacional distingue propósito superior, objetivo retador, visión y misión sin confundirlos.",
                "pregunta": "¿Están los elementos del componente motivacional y se usan correctamente (misión con verbos activos, visión como estado futuro)?",
                "proposito": "El curso los diferencia; confundirlos revela que no se entendió el modelo estratégico.",
            },
        ],
    },
    # ------------------------------------------------------------------
    {
        "id": "modelo_financiero",
        "nombre": "Modelo financiero: estados e interpretación",
        "fuente": "Correcciones del profesor (análisis financiero sobre los modelos)",
        "proposito_dimension": (
            "Verificar que el modelo financiero está bien construido y, sobre todo, "
            "INTERPRETADO y ligado a los demás modelos; el profesor echó de menos "
            "el análisis, no los números."
        ),
        "criterios": [
            {
                "criterio": "Los ingresos son operacionales y se derivan del portafolio de servicios (no se diseñan ingresos no operacionales).",
                "pregunta": "¿Los ingresos salen del portafolio de servicios y se evita diseñar ingresos no operacionales?",
                "proposito": "El profesor fue tajante: 'ingresos operacionales completamente del portafolio de servicios, no diseñar ingresos no operacionales'. Mezclarlos distorsiona la rentabilidad.",
            },
            {
                "criterio": "Los egresos se trazan a procesos, canales, recursos, infraestructura y modelo organizacional, y se identifica el servicio más rentable.",
                "pregunta": "¿Los egresos se derivan de procesos/canales/recursos y se dice cuál servicio es el más rentable?",
                "proposito": "El profesor dijo que los egresos 'se sacan de procesos, canales, recursos, infraestructura, organizacional' y preguntó por el servicio más rentable.",
            },
            {
                "criterio": "Están los tres estados (ingresos-egresos, balance, flujo de caja) y las cuentas del balance explican QUÉ las genera; el capital semilla va al patrimonio.",
                "pregunta": "¿Están los tres estados, el balance explica qué es cada cuenta y el capital de riesgo está en el patrimonio (no en ingresos)?",
                "proposito": "El profesor pidió 'ser explícito de qué son las cuentas' y aclaró que 'el capital semilla va al patrimonio, no a ingresos'. Es un error frecuente que revisa.",
            },
            {
                "criterio": "Los indicadores se INTERPRETAN (no solo se calculan): qué dicen sobre la viabilidad, eficiencia y liquidez del negocio.",
                "pregunta": "¿El documento interpreta los resultados de los indicadores para explicar condiciones del negocio, y no solo los lista?",
                "proposito": "El profesor repitió que 'lo más importante son las conclusiones sobre los indicadores'. Números sin interpretación no valen.",
            },
            {
                "criterio": "El análisis financiero es explícito y se relaciona con el modelo estratégico y el de negocio (canal rentable vs. costoso, línea más rentable).",
                "pregunta": "¿El modelo financiero incluye análisis ligado a la estrategia y al negocio, señalando canal y línea rentables?",
                "proposito": "El profesor anotó 'modelo financiero: falta análisis, que debe relacionarse con el modelo estratégico y de negocio'. El análisis es lo que faltaba.",
            },
        ],
    },
    # ------------------------------------------------------------------
    {
        "id": "competencia",
        "nombre": "Competencia, dolores y viabilidad",
        "fuente": "Correcciones del profesor + análisis estratégico",
        "proposito_dimension": (
            "Verificar que el diseño muestra dolores y competidores, y que compara "
            "DECISIONES DE DISEÑO frente a ellos, no funcionalidades sueltas."
        ),
        "criterios": [
            {
                "criterio": "Se muestran los dolores del cliente y los competidores del negocio.",
                "pregunta": "¿El documento presenta los dolores que resuelve y quiénes son los competidores?",
                "proposito": "El profesor pidió 'mostrar dolores y competidores'. Sin dolor explícito no se justifica el negocio.",
            },
            {
                "criterio": "La comparación con competidores es en términos de DECISIONES DE DISEÑO (canal, capacidad o medio distintos), no de funcionalidades sueltas.",
                "pregunta": "¿Se señala dónde nuestro modelo de negocio toma decisiones de diseño distintas a las de los competidores?",
                "proposito": "El profesor fue específico: comparar 'en términos de decisiones de diseño (canal diferente, capacidad diferente)'. Comparar features es superficial.",
            },
            {
                "criterio": "Se argumenta con datos de mercado qué tan realista es implementar el proyecto.",
                "pregunta": "¿Se usan datos de mercado (ventas, clientes del sector) para evaluar qué tan realista es el proyecto?",
                "proposito": "El profesor pidió 'buscar datos de ventas y clientes actuales' para juzgar la viabilidad. Afirmar viabilidad sin datos es solo opinión.",
            },
        ],
    },
    # ------------------------------------------------------------------
    {
        "id": "vistas",
        "nombre": "Vistas (puntos de vista y componentes de los modelos)",
        "fuente": "Notas de clase (punto de vista = pregunta; vista = instanciación en ArchiMate)",
        "proposito_dimension": (
            "Verificar que cada vista responde a un punto de vista (una pregunta) "
            "coherente con el contexto del negocio y que incluye correctamente los "
            "componentes de los modelos que involucra. Según las notas, un punto de "
            "vista es una pregunta específica que se resuelve a partir de la "
            "estructura del negocio, y una vista es su instanciación (un diagrama "
            "ArchiMate que responde a esa regla)."
        ),
        "criterios": [
            {
                "criterio": "Cada vista responde a un punto de vista o pregunta (regla) coherente y pertinente dentro del contexto del negocio.",
                "pregunta": "¿Cada vista declara su regla/pregunta y esa pregunta es relevante para el negocio (no una pregunta trivial o desconectada)?",
                "proposito": "Según las notas, un punto de vista 'es una pregunta específica que se resuelve a partir de la estructura del negocio'. Una vista sin una pregunta clara no comunica nada ni justifica su existencia.",
            },
            {
                "criterio": "La vista y sus elementos incluyen correctamente los componentes de los diferentes modelos que involucra.",
                "pregunta": "¿La vista contiene los elementos correctos de cada modelo que toca (p. ej. capacidades, servicios, flujos de valor, procesos, objetivos, aplicaciones) y los relaciona bien, sin mezclar niveles ni omitir componentes necesarios para responder la regla?",
                "proposito": "Una vista es la instanciación de un punto de vista: si le faltan componentes de los modelos involucrados o incluye elementos que no corresponden, no responde realmente la pregunta y rompe la trazabilidad entre modelos.",
            },
            {
                "criterio": "El lenguaje y el nivel de abstracción de la vista son los correctos (ArchiMate; solo el nombre del proceso, sin su detalle interno).",
                "pregunta": "¿La vista usa ArchiMate correctamente y respeta el nivel de abstracción (no modela actividades internas de los procesos)?",
                "proposito": "El profesor marcó que en las vistas de ArchiMate solo va el nombre del proceso. Una vista con el detalle interno mezcla niveles y deja de ser una vista de arquitectura.",
            },
        ],
    },
    # ------------------------------------------------------------------
    {
        "id": "trazabilidad",
        "nombre": "Trazabilidad y coherencia entre modelos",
        "fuente": "Notas de clase (trazabilidad, 4 dominios) + correcciones del profesor",
        "proposito_dimension": (
            "Verificar lo transversal que el profesor repitió: que el diseño sea "
            "una arquitectura coherente (los 4 dominios y los modelos se derivan "
            "unos de otros) y que un cambio se pueda rastrear en sus implicaciones."
        ),
        "criterios": [
            {
                "criterio": "El diseño representa el negocio con sus dominios (Negocio, Información, Aplicaciones, TI) de forma articulada.",
                "pregunta": "¿El diseño cubre los dominios del negocio digital y los conecta, en lugar de tratarlos como piezas sueltas?",
                "proposito": "Las notas definen que un negocio digital se representa con 4 dominios; tratarlos aislados rompe la arquitectura.",
            },
            {
                "criterio": "Se reutilizan los canales y recursos ya planteados antes (no se reinventan) e incluye los costos del modelo de negocio base.",
                "pregunta": "¿Los modelos reutilizan canales y recursos definidos antes e incluyen los costos del modelo de negocio base?",
                "proposito": "El profesor pidió 'considerar los canales y recursos ya planteados e incluir los costos del modelo de negocio base'. Diseñar desde cero rompe la continuidad.",
            },
            {
                "criterio": "Se muestra la trazabilidad: cómo un cambio en el modelo de negocio impacta los demás componentes.",
                "pregunta": "¿El documento explica, ante un cambio, qué componentes se ven afectados y cómo?",
                "proposito": "El profesor preguntó '¿cómo nos cambia el modelo de negocio? La trazabilidad, implicaciones en componentes'. La trazabilidad prueba que la arquitectura es coherente.",
            },
            {
                "criterio": "Los modelos se derivan unos de otros sin contradicciones (estrategia → capacidades → operación → financiero).",
                "pregunta": "¿Cada modelo se deriva del anterior y no hay contradicciones entre estrategia, capacidades, operación y finanzas?",
                "proposito": "Es la columna vertebral de la arquitectura de negocio; sin derivación los modelos no forman un diseño, solo una colección de piezas.",
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
    "  - Cumplido: el diseño aborda el criterio de forma clara y bien definida.\n"
    "  - Parcial: lo aborda, pero con vacíos o imprecisiones conceptuales.\n"
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
            f"        Pregunta diagnóstica: {c['pregunta']}\n"
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

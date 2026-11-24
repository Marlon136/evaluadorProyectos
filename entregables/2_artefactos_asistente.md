# Artefactos del asistente de IA

**Curso:** ISIS-2411 Ingeniería de Negocios Digitales — Reemplazo Examen #2
**Entregable 1:** metodología de evaluación, contexto/base de conocimiento, instrucciones/prompts, plataforma utilizada y el diagnóstico generado.

---

## 1. Plataforma utilizada

En lugar de usar una plataforma de IA genérica, se construyó un **asistente propio**: una aplicación web que recibe el PDF del diseño del negocio digital (Taller #3) y devuelve un diagnóstico cualitativo. Componentes:

- **Modelo de IA:** Google Gemini (`gemini-3.1-flash-lite`, con modelos de respaldo ante sobrecarga). Nivel gratuito.
- **Backend:** Python + Flask. Extrae el texto del PDF (`pypdf`), construye el prompt con la metodología y llama al modelo.
- **Frontend:** página web (HTML/CSS/JS) para subir el PDF y visualizar el diagnóstico.
- **Despliegue:** preparado para Render (`render.yaml`, `gunicorn`).

Archivos clave: `rubrica.py` (metodología), `evaluador.py` (prompts y llamada al modelo), `app.py` (servidor), `templates/` y `static/` (interfaz).

## 2. Metodología de evaluación

La metodología completa (dimensiones, criterios, **pregunta diagnóstica** y **propósito** de cada criterio) está en `1_metodologia_criterios.pdf`, generado desde el código del asistente (`rubrica.py`), por lo que refleja exactamente lo que aplica.

### De dónde salieron los criterios (y por qué son propios)

Los criterios NO son genéricos ni la rúbrica oficial. Se construyeron a partir de tres fuentes concretas de nuestro propio trabajo:

1. **Nuestras notas de clase**, con las definiciones textuales del curso: "no toda acción es servicio de negocio: debe cumplir acción, genera valor, monetización", "flujo de valor = secuencia de capacidades que permite entregar un servicio", "el mapa no tiene capacidades duplicadas", "recursos (con qué) vs. medios (por dónde)", los tipos de actor (cliente/usuario/prospecto/temporal), los 4 dominios (Negocio, Información, Aplicaciones, TI), la frontera digital, etc.
2. **Las correcciones que el profesor nos hizo** sobre el diseño: "la capacidad crítica se reusa entre flujos", "no diseñar ingresos no operacionales", "la tecnología tiene que escalar y ser de bajo acoplamiento", "en las vistas de Archi solo va el nombre del proceso", "el capital semilla va al patrimonio, no a ingresos", "comparar con competidores por decisiones de diseño".
3. **Las lecturas del curso** (Arquitectura de Negocio) y *Playing to Win*.

Por eso cada criterio trae una **pregunta diagnóstica**: la pregunta exacta que se hace al revisar, que el asistente responde con evidencia del documento.

**Las 10 dimensiones** (organizadas por los elementos y modelos de la arquitectura de negocio del curso):

1. **Servicios de negocio y objeto de valor** — un servicio es una acción que genera valor y monetiza; objeto tipificado; líneas de negocio.
2. **Estructura de negocio: actores y canales** — cliente/usuario/prospecto/temporal; canales directos/indirectos; recursos vs. medios.
3. **Escenarios de negocio** — cuentan la historia con el orden temporal; cuál impacta más.
4. **Capacidades, flujos de valor y capacidad crítica** — flujo de valor = secuencia de capacidades; capacidad crítica reusada; mapa sin duplicados.
5. **Modelo operativo** — procesos vs. procedimientos; qué proceso apoya qué servicio; reglas de modelado en Archi.
6. **Aplicaciones y tecnología** — dueño de la información, escalabilidad, bajo acoplamiento, bus; separación de dominios.
7. **Modelo estratégico y prioridad** — prioridad estratégica, cómo ganar, componente motivacional.
8. **Modelo financiero** — tres estados, interpretación de indicadores y análisis ligado a estrategia y negocio.
9. **Competencia, dolores y viabilidad** — comparación por decisiones de diseño y datos de mercado.
10. **Trazabilidad y coherencia entre modelos** — los 4 dominios articulados e implicaciones de un cambio.

### Cumplimiento de las reglas del enunciado

- **Regla a (criterios propios, no la rúbrica oficial):** los criterios son de elaboración propia, apoyados en las lecturas del curso (Arquitectura de Negocio) y en *Playing to Win*. No se usó ni se cargó la rúbrica oficial de los talleres.
- **Regla b (sobre el Taller #3 preliminar):** el asistente recibe como entrada el PDF del Taller #3 del grupo antes de la entrega final.
- **Regla c (diagnóstico cualitativo, sin nota numérica):** la salida usa niveles cualitativos (Cumplido / Parcial / Incipiente / Ausente / No aplica) y texto; no hay puntajes, notas ni porcentajes.

## 3. Contexto / base de conocimiento cargada

El asistente **no recibe la rúbrica oficial** como contexto. El contexto que se inyecta al modelo es:

1. La **metodología propia** (dimensiones, criterios y propósitos) desde `rubrica.py`.
2. Los **niveles de cumplimiento cualitativos**.
3. El **texto del PDF del diseño** del negocio (Taller #3), extraído automáticamente.

La base conceptual (lo aprendido en el curso) está incorporada en la redacción de los criterios y en el rol del sistema, no como documentos cargados.

## 4. Instrucciones / prompts

El asistente usa dos mensajes. El contenido exacto se genera en `evaluador.py`:

### Mensaje de sistema (rol del asistente)

> Actúas como evaluador e ingeniero de negocios digitales. Evalúas la versión preliminar del DISEÑO de un negocio digital (Talleres #1 a #3) y entregas un DIAGNÓSTICO CUALITATIVO, con rigor técnico y tono profesional, objetivo y constructivo. Usas únicamente los marcos de la metodología provista. REGLA ABSOLUTA: NO asignes calificaciones numéricas, puntajes, notas ni porcentajes de ningún tipo; el diagnóstico es puramente cualitativo mediante las etiquetas de nivel definidas. Si el documento no aporta información para un criterio, dilo explícitamente y usa el nivel 'Ausente' o 'Incipiente'. No inventes datos del negocio que no estén en el documento; para el análisis competitivo sí puedes citar empresas reales del mercado.

### Mensaje de usuario (tarea)

Incluye, en este orden:
1. La metodología completa (dimensiones, criterios y su propósito).
2. Los niveles de cumplimiento cualitativos.
3. Instrucciones: evaluar cada criterio con un nivel y un hallazgo; dar nivel y diagnóstico por dimensión; análisis competitivo con empresas reales; resumen y valoración global en palabras; riesgos y cambios prioritarios; prohibición explícita de usar números; y el esquema JSON exacto de la respuesta.
4. El texto del documento del Taller #3.

El prompt literal y actualizado se puede imprimir con:

```bash
python -c "from evaluador import _construir_prompt; s,u=_construir_prompt('<texto del Taller 3>'); print(s); print(u)"
```

## 5. Diagnóstico completo generado por el asistente

El diagnóstico completo que generó el asistente sobre el Taller #3 se adjunta en `3_diagnostico_generado.md` (texto) y puede reproducirse ejecutando el asistente sobre el PDF del Taller #3.

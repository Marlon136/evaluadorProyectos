<!--
INFORME EJECUTIVO - ENTREGABLE 2 (máximo 3 páginas)
==================================================
Vale el 40% y se evalúa por: interpretación con criterio propio, cambios
concretos derivados de los hallazgos, y comprensión profunda del diseño.

Este borrador ya está lleno con el negocio real (NutriA) y con el diagnóstico
que generó el asistente. REVÍSALO y ponlo en TUS palabras: el profesor valora la
interpretación propia, no el texto del asistente copiado.

IMPORTANTE: el asistente evaluó la versión que le pasaste y salió "Cumplido" en
casi todo porque es una versión ya pulida. El enunciado pide correrlo sobre la
versión PRELIMINAR (antes de la entrega final). Si tienes una versión más
temprana del Taller #3, córrela con:
    python generar_diagnostico.py ruta/a/version_preliminar.pdf
y ahí saldrán hallazgos de mejora reales para enriquecer este análisis.
-->

# Informe ejecutivo — Análisis de resultados

**Negocio digital:** NutriA (FoodTech de kits de comida saludable porcionados)
**Grupo 5:** Laura Sofía Barrero (202311190), Marlon Londoño (202317352), Jose Daniel Carvajal (202317192)
**Curso:** ISIS-2411 Ingeniería de Negocios Digitales — Reemplazo Examen #2

---

## 1. Qué hicimos

Construimos un asistente de IA (aplicación web propia sobre Google Gemini) con una metodología de evaluación de 11 dimensiones y 45 criterios, cada uno con su propósito explícito. Los criterios los definimos a partir de las correcciones que el profesor nos hizo en clase, de nuestras notas del curso y de las lecturas de Arquitectura de Negocio; no usamos la rúbrica oficial de los talleres. Ejecutamos el asistente sobre el documento del Taller #3 de NutriA y obtuvimos un diagnóstico cualitativo (sin calificación numérica). Este informe interpreta ese diagnóstico y define los cambios que haremos antes de la entrega final.

## 2. Síntesis del diagnóstico obtenido

El asistente valoró el diseño como *"de alta madurez y coherencia estructural"*: una arquitectura de negocio que articula estrategia, capacidades, operación y tecnología, con un modelo financiero coherente con la estrategia. Las 11 dimensiones quedaron en nivel *Cumplido*. Los puntos fuertes que destacó: la distinción técnica correcta entre recursos y medios, el mapa de capacidades sin duplicados con capacidades críticas justificadas, la arquitectura de TI con bus de integración y bajo acoplamiento, y el modelo financiero con indicadores interpretados.

> _Comenta aquí si coincides: ¿el diseño está tan sólido como dice el asistente, o hay partes donde el diagnóstico fue condescendiente y tú sabes que falta trabajo?_

## 3. Interpretación propia de los hallazgos

Aunque el nivel general es alto, el diagnóstico dejó ver tres frentes donde el diseño es más vulnerable de lo que parece. Interpretamos cada uno:

- **Cadena de frío en la expansión multiciudad.** El asistente lo marcó como riesgo, no como defecto del modelo. Nuestra lectura: la ventaja competitiva de NutriA (producción propia certificada + kit congelado) depende de una cadena de frío que hoy está probada para una sola cocina en Bogotá. Al abrir Medellín, Cali y Barranquilla (AE-01 a AE-03), ese diferencial se vuelve el punto más frágil, porque un fallo de frío rompe a la vez la promesa de calidad (V1) y la de confianza (V2).
- **Retención de NutriA Kids por estacionalidad.** El modelo asume churn bajo en S6, pero el servicio se pausa en vacaciones (diciembre y enero). Nuestra lectura: la meta de 20% de ventas en NutriA Kids (IND-04) es sensible a que los padres no renueven tras la pausa; el diseño de retención post-vacaciones está poco desarrollado frente a lo detallado que está el resto.
- **Rentabilidad del servicio ocasional S4.** El margen de contribución de S4 (kit día) es 32,9%, muy por debajo del resto (44-50%). Nuestra lectura: aunque S4 funciona como puerta de entrada a la suscripción, conviene revisar si su precio o su costo logístico lo hacen sostenible por sí solo o si solo se justifica como gancho de adquisición.

> _Agrega o ajusta los hallazgos según lo que ustedes vean. Si corren la versión preliminar, trae aquí los vacíos que esa versión tenía y que ya corrigieron._

## 4. Cambios concretos que haremos en el diseño

| # | Cambio concreto | Hallazgo que lo origina | Dimensión |
|---|---|---|---|
| 1 | Añadir al modelo operativo un procedimiento de contingencia de cadena de frío por ciudad (umbral de temperatura, responsable, acción) y un indicador de incidentes de frío por cocina | Riesgo de cadena de frío en expansión | Modelo operativo / Capacidades |
| 2 | Diseñar una acción estratégica de reactivación de NutriA Kids al terminar vacaciones (recordatorio, incentivo de renovación) ligada a IND-04 | Retención de NutriA Kids por estacionalidad | Modelo estratégico / Financiero |
| 3 | Revisar el precio y el costo logístico de S4 (kit día) o reposicionarlo explícitamente como servicio gancho, no como línea rentable | Margen bajo de S4 (32,9%) | Servicios / Financiero |
| 4 | _[si corren la versión preliminar, listar aquí los vacíos que el asistente encontró y cómo los cerraron]_ | | |

## 5. Comprensión del diseño y conclusión

NutriA es un diseño maduro cuya fortaleza es la coherencia entre modelos: la estrategia de integración vertical y personalización se refleja en las capacidades críticas (preparación y porcionado, calidad e inocuidad), estas en la operación (procesos PM-06 y PM-07) y todo se mide con indicadores que llegan hasta la capa de TI. El diagnóstico confirma que la arquitectura está bien construida. El trabajo pendiente no está en completar modelos, sino en blindar el punto donde el diferencial es más frágil —la cadena de frío al escalar— y en afinar dos decisiones de negocio (retención estacional de NutriA Kids y rentabilidad del servicio ocasional). Esos ajustes elevan la robustez del diseño sin alterar su estructura, que ya es sólida.

> _Cierra con tu propia conclusión. Máximo 3 páginas en total; recorta lo que no uses._

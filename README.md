# Evaluador de Negocios Digitales

# Asistente de diagnóstico de negocios digitales

Ejercicio ISIS-2411 (Reemplazo Examen #2). Aplicación web que recibe el **PDF**
del diseño de un negocio digital (Taller #3), lo analiza con un modelo de IA
según una **metodología propia** apoyada en las lecturas del curso de
Arquitectura de Negocio y en *Playing to Win* (Lafley & Martin), y devuelve un
**diagnóstico cualitativo** (sin calificación numérica).

> Los entregables del ejercicio están en la carpeta `entregables/`
> (ver `entregables/README_ENTREGABLES.md`).

## ¿Qué evalúa?

La metodología (ver `rubrica.py`) tiene 7 dimensiones. Cada criterio declara su
**propósito** (qué verifica y por qué importa):

| Dimensión | Base conceptual |
|-----------|-----------------|
| Modelo de negocio | El Modelo de Negocio |
| Propuesta / promesa de valor | Modelo de Negocio + Modelo Estratégico |
| Modelo estratégico y cascada de decisiones | El Modelo Estratégico + Playing to Win |
| Capacidades de negocio | El Mapa de Capacidades |
| Clientes, mercado y entorno competitivo | Análisis Estratégico (Porter, PEST) |
| Viabilidad financiera y operativa | Análisis Estratégico (financiero, TI, riesgos) |
| Completitud y coherencia de los modelos del negocio | Arquitectura de Negocio |

El diagnóstico es **cualitativo**: cada dimensión y cada criterio recibe un
nivel (Cumplido / Parcial / Incipiente / Ausente / No aplica), con hallazgos,
fortalezas, debilidades y cambios sugeridos. Incluye también un **análisis
competitivo** (empresas reales comparables, diferenciadores, posicionamiento) y
una lista de **cambios prioritarios** sobre el diseño. No hay puntajes ni notas.

## Proveedor de IA: Google Gemini (gratis)

La app usa **Google Gemini**, que tiene un nivel gratuito.

1. Crea una clave en https://aistudio.google.com/app/apikey
2. Ponla en la variable de entorno `GEMINI_API_KEY`.

## Ejecutar en local

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

cp .env.example .env   # y pega tu GEMINI_API_KEY
python app.py
```

Abre http://localhost:5000, sube un PDF y evalúa.

## Desplegar en Render

1. Sube este repositorio a GitHub.
2. En [Render](https://render.com) crea un **New > Blueprint** y apunta al repo.
   Render leerá `render.yaml` automáticamente.
3. En las variables de entorno del servicio, define `GEMINI_API_KEY`. Está
   marcada como `sync: false`, por eso se pide manualmente (no se sube al repo).
4. Deploy. El servicio arranca con `gunicorn app:app`.

Alternativa manual (sin blueprint): crea un **Web Service**, runtime Python,
`buildCommand: pip install -r requirements.txt`,
`startCommand: gunicorn app:app`, y agrega la variable `GEMINI_API_KEY`.

## Estructura

```
app.py            # servidor Flask (rutas / , /evaluar , /health)
evaluador.py      # extracción de PDF + llamada al LLM + normalización
rubrica.py        # dimensiones, pesos y criterios de evaluación
templates/        # index.html
static/           # styles.css , app.js
render.yaml       # configuración de despliegue en Render
requirements.txt
```

## Notas

- El PDF debe contener **texto** (no imágenes escaneadas). Para escaneados se
  necesitaría OCR, que no está incluido.
- El texto del documento se trunca a `MAX_PDF_CHARS` (60.000 por defecto) para
  no exceder el contexto del modelo.
# evaluadorProyectos

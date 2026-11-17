# Evaluador de Negocios Digitales

Aplicación web que recibe el **PDF** de un negocio digital, lo evalúa con un
modelo de IA según una **rúbrica profesional** derivada de las lecturas del
curso de Arquitectura de Negocio y de *Playing to Win* (Lafley & Martin), y
devuelve una evaluación estructurada.

## ¿Qué evalúa?

La rúbrica (ver `rubrica.py`) tiene 6 dimensiones ponderadas:

| Dimensión | Peso | Base conceptual |
|-----------|------|-----------------|
| Modelo de negocio | 20% | Lectura #2 – El Modelo de Negocio |
| Propuesta / promesa de valor | 18% | Modelo de Negocio + Modelo Estratégico |
| Modelo estratégico y cascada de decisiones | 20% | El Modelo Estratégico + Playing to Win |
| Capacidades de negocio | 12% | Lectura #1 – El Mapa de Capacidades |
| Clientes, mercado y entorno competitivo | 15% | Análisis Estratégico (Porter, PEST) |
| Viabilidad financiera y operativa | 15% | Análisis Estratégico (financiero, TI, riesgos) |

Además de calificar las dimensiones (0 a 5) y dar un **puntaje global 0-100**,
nivel, veredicto y resumen ejecutivo, la evaluación incluye un **análisis
competitivo**: identifica productos/empresas reales similares del mercado, qué
hacen mejor, qué **diferencia** al negocio evaluado, si tiene una ventaja
competitiva sostenible (moat) y su posicionamiento.

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

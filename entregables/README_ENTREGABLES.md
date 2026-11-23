# Entregables — Reemplazo Examen #2 (ISIS-2411)

Qué pide el enunciado y dónde está cada cosa. Entrega: **un único `.zip` por BNe**, antes del **lunes 23 de noviembre de 2026**.

## Mapeo enunciado → archivos

**Entregable 1 — Artefactos del asistente IA:**
- `2_artefactos_asistente.md` — documento guía: plataforma, metodología, contexto, prompts y referencias.
- `1_metodologia_criterios.pdf` — metodología completa: las 7 dimensiones, sus criterios y el **propósito** de cada uno (generado desde el código del asistente).
- `3_diagnostico_generado.md` — el diagnóstico completo que generó el asistente sobre el Taller #3.
- El código del asistente (carpeta raíz del proyecto): `rubrica.py`, `evaluador.py`, `app.py`, `templates/`, `static/`.

**Entregable 2 — Análisis de resultados (informe ejecutivo, máx. 3 páginas):**
- `4_informe_ejecutivo.md` — plantilla a completar con tu interpretación propia y los cambios al diseño.

## Qué debes hacer tú (no automatizable)

1. **Correr el asistente sobre tu Taller #3 real:**
   ```bash
   python generar_diagnostico.py ruta/al/TU_Taller3.pdf
   ```
   Esto regenera `3_diagnostico_generado.md` con tu negocio real.

2. **Escribir el informe ejecutivo** (`4_informe_ejecutivo.md`) con tu interpretación y cambios, en máximo 3 páginas. Exportarlo a PDF si lo prefieres.

3. **Regenerar el PDF de metodología** si cambiaste criterios:
   ```bash
   python generar_pdf_criterios.py
   ```

## Cómo armar el .zip

Incluye en el zip:
- Los 4 documentos de `entregables/`.
- El código del asistente (todo el proyecto, sin `.venv/`, `__pycache__/`, ni `.env`).

> No incluyas el archivo `.env` (contiene la clave de API) ni `lecturas_texto/`.

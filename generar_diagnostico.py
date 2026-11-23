"""Ejecuta el asistente sobre un PDF (el Taller #3) y guarda el diagnóstico
completo como documento Markdown, para el entregable 3.

Uso:
    python generar_diagnostico.py ruta/al/Taller3.pdf

Salida: entregables/3_diagnostico_generado.md
"""
import sys
from datetime import date

from dotenv import load_dotenv

from evaluador import evaluar_pdf

load_dotenv()

SALIDA = "entregables/3_diagnostico_generado.md"


def _lista(items, vacio="(ninguno)"):
    items = items or []
    if not items:
        return f"- {vacio}\n"
    return "".join(f"- {x}\n" for x in items)


def a_markdown(res: dict) -> str:
    out = []
    out.append("# Diagnóstico generado por el asistente de IA\n")
    out.append(
        f"**Negocio:** {res.get('nombre_negocio', 'No especificado')}  \n"
        f"**Fecha:** {date.today().strftime('%d/%m/%Y')}  \n"
        f"**Tipo de salida:** diagnóstico cualitativo (sin calificación numérica)\n"
    )
    out.append(f"\n**Valoración global:** {res.get('valoracion_global', '')}\n")
    out.append(f"\n{res.get('resumen_diagnostico', '')}\n")

    out.append("\n## Diagnóstico por dimensión\n")
    for d in res.get("dimensiones", []):
        out.append(f"\n### {d.get('nombre')} — *{d.get('nivel')}*\n")
        out.append(f"{d.get('diagnostico', '')}\n")
        if d.get("criterios"):
            out.append("\n| Criterio | Nivel | Hallazgo |\n|---|---|---|\n")
            for c in d["criterios"]:
                crit = str(c.get("criterio", "")).replace("|", "\\|")
                hall = str(c.get("hallazgo", "")).replace("|", "\\|")
                out.append(f"| {crit} | {c.get('nivel','')} | {hall} |\n")
        out.append("\n**Fortalezas:**\n")
        out.append(_lista(d.get("fortalezas")))
        out.append("\n**Debilidades:**\n")
        out.append(_lista(d.get("debilidades")))
        out.append("\n**Cambios sugeridos:**\n")
        out.append(_lista(d.get("recomendaciones")))

    comp = res.get("analisis_competitivo") or {}
    if comp:
        out.append("\n## Análisis competitivo\n")
        out.append(f"{comp.get('resumen', '')}\n")
        for c in comp.get("competidores", []):
            out.append(
                f"\n- **{c.get('nombre')}** — {c.get('descripcion')}  \n"
                f"  Similitud: {c.get('similitud')}  \n"
                f"  Su ventaja: {c.get('ventaja_de_ellos')}\n"
            )
        out.append("\n**Diferenciadores del negocio:**\n")
        out.append(_lista(comp.get("diferenciadores")))
        if comp.get("ventaja_competitiva_sostenible"):
            out.append(
                f"\n**Ventaja competitiva sostenible:** "
                f"{comp.get('ventaja_competitiva_sostenible')}\n"
            )
        out.append(f"\n**Posicionamiento:** {comp.get('posicionamiento', '')}\n")

    out.append("\n## Riesgos principales\n")
    out.append(_lista(res.get("riesgos_principales")))
    out.append("\n## Cambios prioritarios sobre el diseño\n")
    out.append(_lista(res.get("cambios_prioritarios")))

    return "".join(out)


def main():
    if len(sys.argv) < 2:
        print("Uso: python generar_diagnostico.py ruta/al/Taller3.pdf")
        sys.exit(1)
    ruta = sys.argv[1]
    with open(ruta, "rb") as f:
        res = evaluar_pdf(f.read())
    with open(SALIDA, "w", encoding="utf-8") as w:
        w.write(a_markdown(res))
    print(f"Diagnóstico guardado en: {SALIDA}")


if __name__ == "__main__":
    main()

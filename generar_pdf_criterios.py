"""Genera un PDF con la metodología de evaluación a partir de rubrica.py.

El PDF se construye desde la fuente de verdad (DIMENSIONES, ESCALA), así que
siempre refleja lo que el asistente usa realmente. Es el entregable
"metodología de evaluación (criterios y propósito de cada uno)".

Uso:  .venv/bin/python generar_pdf_criterios.py
Salida: entregables/1_metodologia_criterios.pdf
"""
import os
from datetime import date

from reportlab.lib import colors
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import (
    HRFlowable,
    ListFlowable,
    ListItem,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

from rubrica import DIMENSIONES, ESCALA, NIVELES

SALIDA = "entregables/1_metodologia_criterios.pdf"

AZUL = colors.HexColor("#1f3a8a")
VERDE = colors.HexColor("#0f8a6a")
GRIS = colors.HexColor("#555b73")
GRIS_CLARO = colors.HexColor("#eef1f8")


def estilos():
    base = getSampleStyleSheet()
    s = {}
    s["titulo"] = ParagraphStyle(
        "titulo", parent=base["Title"], fontSize=22, textColor=AZUL,
        spaceAfter=6, leading=26,
    )
    s["subtitulo"] = ParagraphStyle(
        "subtitulo", parent=base["Normal"], fontSize=11, textColor=GRIS,
        spaceAfter=16, leading=15,
    )
    s["h2"] = ParagraphStyle(
        "h2", parent=base["Heading2"], fontSize=14, textColor=AZUL,
        spaceBefore=14, spaceAfter=6,
    )
    s["dim_titulo"] = ParagraphStyle(
        "dim_titulo", parent=base["Heading2"], fontSize=13,
        textColor=colors.white, spaceBefore=0, spaceAfter=0, leading=16,
    )
    s["fuente"] = ParagraphStyle(
        "fuente", parent=base["Normal"], fontSize=9, textColor=GRIS,
        spaceBefore=4, spaceAfter=2,
    )
    s["prop_dim"] = ParagraphStyle(
        "prop_dim", parent=base["Normal"], fontSize=9.5, textColor=GRIS,
        leading=13, spaceAfter=6, alignment=TA_JUSTIFY,
    )
    s["cuerpo"] = ParagraphStyle(
        "cuerpo", parent=base["Normal"], fontSize=10.5, leading=15,
        alignment=TA_JUSTIFY, spaceAfter=6,
    )
    s["crit"] = ParagraphStyle(
        "crit", parent=base["Normal"], fontSize=10, leading=13.5,
        alignment=TA_LEFT,
    )
    s["prop"] = ParagraphStyle(
        "prop", parent=base["Normal"], fontSize=9, leading=12.5,
        textColor=GRIS, alignment=TA_LEFT, leftIndent=10, spaceAfter=4,
    )
    s["escala"] = ParagraphStyle(
        "escala", parent=base["Normal"], fontSize=10, leading=15,
    )
    s["nota"] = ParagraphStyle(
        "nota", parent=base["Normal"], fontSize=9.5, textColor=GRIS,
        leading=14,
    )
    return s


def banda_dimension(dim, st):
    nombre = Paragraph(dim["nombre"], st["dim_titulo"])
    t = Table([[nombre]], colWidths=[16.5 * cm])
    t.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), AZUL),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("LEFTPADDING", (0, 0), (-1, -1), 10),
                ("TOPPADDING", (0, 0), (-1, -1), 7),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
            ]
        )
    )
    return t


def construir():
    st = estilos()
    os.makedirs(os.path.dirname(SALIDA), exist_ok=True)
    doc = SimpleDocTemplate(
        SALIDA, pagesize=letter,
        leftMargin=2.2 * cm, rightMargin=2.2 * cm,
        topMargin=2 * cm, bottomMargin=2 * cm,
        title="Metodología de evaluación - Asistente IA",
    )
    flow = []

    flow.append(Paragraph("Metodología de evaluación", st["titulo"]))
    flow.append(
        Paragraph(
            "Asistente de IA para diagnóstico cualitativo de negocios digitales · "
            "ISIS-2411 Ingeniería de Negocios Digitales · "
            f"Actualizado el {date.today().strftime('%d/%m/%Y')}",
            st["subtitulo"],
        )
    )
    flow.append(HRFlowable(width="100%", color=VERDE, thickness=2))
    flow.append(Spacer(1, 10))
    flow.append(
        Paragraph(
            "Este documento define la metodología que usa el asistente para "
            "diagnosticar la versión preliminar del diseño de un negocio "
            "digital (Talleres #1 a #3). El diagnóstico es <b>cualitativo, sin "
            "calificación numérica</b>. Los criterios son propios y NO "
            "corresponden a la rúbrica oficial de los talleres; se apoyan en lo "
            "aprendido en el curso (Arquitectura de Negocio) y en <i>Playing to "
            "Win</i> (Lafley &amp; Martin). Cada criterio incluye su "
            "<b>propósito</b>: qué se verifica y por qué importa en un negocio "
            "digital.",
            st["cuerpo"],
        )
    )

    # Niveles cualitativos
    flow.append(Paragraph("Niveles de cumplimiento (cualitativos)", st["h2"]))
    for linea in ESCALA.split("\n"):
        linea = linea.strip()
        if not linea:
            continue
        if linea.startswith("-"):
            flow.append(Paragraph(f"&nbsp;&nbsp;{linea}", st["escala"]))
        else:
            flow.append(Paragraph(linea, st["nota"]))

    flow.append(PageBreak())

    # Detalle por dimensión
    flow.append(Paragraph("Dimensiones, criterios y su propósito", st["h2"]))
    flow.append(Spacer(1, 4))
    for d in DIMENSIONES:
        flow.append(banda_dimension(d, st))
        flow.append(Paragraph(f"Fuente: {d['fuente']}", st["fuente"]))
        flow.append(
            Paragraph(
                f"<b>Propósito de la dimensión:</b> {d['proposito_dimension']}",
                st["prop_dim"],
            )
        )
        items = []
        for c in d["criterios"]:
            items.append(ListItem(Paragraph(c["criterio"], st["crit"]),
                                  leftIndent=6))
        flow.append(
            ListFlowable(
                items, bulletType="bullet", bulletColor=VERDE,
                bulletFontSize=7, leftIndent=12, spaceBefore=2,
            )
        )
        # Propósito de cada criterio, debajo de la lista.
        for c in d["criterios"]:
            flow.append(
                Paragraph(
                    f"↳ <i>Propósito:</i> {c['proposito']}", st["prop"]
                )
            )
        flow.append(Spacer(1, 12))

    doc.build(flow)
    return SALIDA


if __name__ == "__main__":
    ruta = construir()
    print(f"PDF generado: {ruta}")

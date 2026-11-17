"""Aplicación web Flask para evaluar negocios digitales a partir de un PDF."""
import os

from dotenv import load_dotenv
from flask import Flask, jsonify, render_template, request

from evaluador import ErrorEvaluacion, evaluar_pdf

load_dotenv()

app = Flask(__name__)
# Límite de tamaño de subida (por defecto 16 MB).
app.config["MAX_CONTENT_LENGTH"] = int(
    os.environ.get("MAX_UPLOAD_BYTES", str(16 * 1024 * 1024))
)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


@app.route("/evaluar", methods=["POST"])
def evaluar():
    archivo = request.files.get("pdf")
    if archivo is None or archivo.filename == "":
        return jsonify({"error": "No se recibió ningún archivo PDF."}), 400

    if not archivo.filename.lower().endswith(".pdf"):
        return jsonify({"error": "El archivo debe ser un PDF."}), 400

    datos = archivo.read()
    if not datos:
        return jsonify({"error": "El archivo está vacío."}), 400

    try:
        resultado = evaluar_pdf(datos)
    except ErrorEvaluacion as exc:
        return jsonify({"error": str(exc)}), 400
    except Exception:  # noqa: BLE001
        app.logger.exception("Error inesperado al evaluar")
        return jsonify({"error": "Ocurrió un error inesperado al evaluar."}), 500

    return jsonify(resultado)


@app.errorhandler(413)
def demasiado_grande(_):
    return jsonify({"error": "El archivo es demasiado grande."}), 413


if __name__ == "__main__":
    puerto = int(os.environ.get("PORT", "5000"))
    app.run(host="0.0.0.0", port=puerto, debug=True)

const form = document.getElementById("form");
const input = document.getElementById("pdf");
const dropzone = document.getElementById("dropzone");
const dzText = document.getElementById("dz-text");
const btn = document.getElementById("btn");
const loading = document.getElementById("loading");
const loadingText = document.getElementById("loading-text");
const errorBox = document.getElementById("error");
const resultado = document.getElementById("resultado");

function setFile(file) {
  if (file && file.type === "application/pdf") {
    const dt = new DataTransfer();
    dt.items.add(file);
    input.files = dt.files;
    dzText.textContent = file.name;
    dzText.classList.add("has-file");
    btn.disabled = false;
  }
}

input.addEventListener("change", () => {
  if (input.files.length) setFile(input.files[0]);
});

["dragenter", "dragover"].forEach((e) =>
  dropzone.addEventListener(e, (ev) => {
    ev.preventDefault();
    dropzone.classList.add("dragover");
  })
);
["dragleave", "drop"].forEach((e) =>
  dropzone.addEventListener(e, (ev) => {
    ev.preventDefault();
    dropzone.classList.remove("dragover");
  })
);
dropzone.addEventListener("drop", (ev) => setFile(ev.dataTransfer.files[0]));

const steps = [
  "Extrayendo el texto del documento…",
  "Analizando modelo de negocio y propuesta de valor…",
  "Evaluando estrategia y capacidades…",
  "Comparando con competidores del mercado…",
  "Redactando el diagnóstico cualitativo…",
];
let stepTimer = null;
function startSteps() {
  let i = 0;
  loadingText.textContent = steps[0];
  stepTimer = setInterval(() => {
    i = (i + 1) % steps.length;
    loadingText.textContent = steps[i];
  }, 2600);
}
function stopSteps() {
  if (stepTimer) clearInterval(stepTimer);
}

form.addEventListener("submit", async (ev) => {
  ev.preventDefault();
  if (!input.files.length) return;

  errorBox.classList.add("hidden");
  resultado.classList.add("hidden");
  loading.classList.remove("hidden");
  startSteps();
  btn.disabled = true;

  const data = new FormData();
  data.append("pdf", input.files[0]);

  try {
    const resp = await fetch("/evaluar", { method: "POST", body: data });
    const json = await resp.json();
    if (!resp.ok) throw new Error(json.error || "Error al evaluar.");
    render(json);
  } catch (err) {
    errorBox.textContent = err.message;
    errorBox.classList.remove("hidden");
  } finally {
    stopSteps();
    loading.classList.add("hidden");
    btn.disabled = false;
  }
});

function esc(str) {
  const d = document.createElement("div");
  d.textContent = str == null ? "" : String(str);
  return d.innerHTML;
}

function list(items) {
  if (!items || !items.length) return "<p class='just'>Sin elementos.</p>";
  return `<ul>${items.map((i) => `<li>${esc(i)}</li>`).join("")}</ul>`;
}

// Clase CSS según el nivel cualitativo (sin números).
function nivelClase(nivel) {
  const n = (nivel || "").toLowerCase();
  if (n.startsWith("cumpl")) return "lvl-ok";
  if (n.startsWith("parcial")) return "lvl-mid";
  if (n.startsWith("incipi")) return "lvl-low";
  if (n.startsWith("ausente")) return "lvl-bad";
  return "lvl-na";
}

function render(data) {
  const dims = (data.dimensiones || [])
    .map((d) => {
      const crits = (d.criterios || [])
        .map(
          (c) => `
          <li class="crit-row">
            <span class="lvl-tag ${nivelClase(c.nivel)}">${esc(c.nivel)}</span>
            <span class="crit-text"><b>${esc(c.criterio)}</b> ${esc(c.hallazgo)}</span>
          </li>`
        )
        .join("");
      return `
      <div class="dim card">
        <div class="dim-head">
          <h4>${esc(d.nombre)}</h4>
          <span class="lvl-tag ${nivelClase(d.nivel)}">${esc(d.nivel)}</span>
        </div>
        <p class="just">${esc(d.diagnostico)}</p>
        ${crits ? `<ul class="crit-list">${crits}</ul>` : ""}
        <div class="lists">
          <div class="block pos"><h5>Fortalezas</h5>${list(d.fortalezas)}</div>
          <div class="block neg"><h5>Debilidades</h5>${list(d.debilidades)}</div>
          <div class="block rec"><h5>Cambios sugeridos</h5>${list(d.recomendaciones)}</div>
        </div>
      </div>`;
    })
    .join("");

  const comp = data.analisis_competitivo || {};
  const competidores = (comp.competidores || [])
    .map(
      (c) => `
      <div class="competitor">
        <h5>${esc(c.nombre)}</h5>
        <p class="desc">${esc(c.descripcion)}</p>
        <p class="kv"><b>Similitud:</b> ${esc(c.similitud)}</p>
        <p class="kv adv"><b>Su ventaja:</b> ${esc(c.ventaja_de_ellos)}</p>
      </div>`
    )
    .join("");

  const compHtml = comp && (comp.competidores || comp.diferenciadores)
    ? `
    <h3 class="section-title">Análisis competitivo y diferenciación</h3>
    <div class="comp-wrap card">
      <p class="lead">${esc(comp.resumen || "")}</p>
      <div class="comp-grid">${competidores || "<p class='just'>No se identificaron competidores.</p>"}</div>
      <div class="diff-box">
        <div class="panel-inner">
          <h5>Qué lo diferencia</h5>
          ${list(comp.diferenciadores)}
        </div>
        <div class="panel-inner">
          <h5>Posicionamiento</h5>
          <p class="just" style="margin:0">${esc(comp.posicionamiento || "No determinado")}</p>
        </div>
      </div>
      ${
        comp.ventaja_competitiva_sostenible
          ? `<div class="moat"><h5>Ventaja competitiva sostenible (moat)</h5><p>${esc(comp.ventaja_competitiva_sostenible)}</p></div>`
          : ""
      }
    </div>`
    : "";

  resultado.innerHTML = `
    <div class="diag-card card">
      <div class="row">
        <span class="badge">Diagnóstico cualitativo</span>
        ${data.nombre_negocio ? `<span class="biz-name">• ${esc(data.nombre_negocio)}</span>` : ""}
      </div>
      <h2>Diagnóstico del diseño</h2>
      ${data.valoracion_global ? `<p class="verdict">▸ ${esc(data.valoracion_global)}</p>` : ""}
      <p class="summary">${esc(data.resumen_diagnostico || "")}</p>
    </div>

    <h3 class="section-title">Diagnóstico por dimensión</h3>
    <div class="dims">${dims}</div>

    ${compHtml}

    <h3 class="section-title">Riesgos principales</h3>
    <div class="panel card">${list(data.riesgos_principales)}</div>

    <h3 class="section-title">Cambios prioritarios sobre el diseño</h3>
    <div class="panel card">${list(data.cambios_prioritarios)}</div>

    <div class="actions">
      <button class="btn-secondary" id="again">Evaluar otro documento</button>
    </div>
  `;

  resultado.classList.remove("hidden");
  document.getElementById("again").addEventListener("click", () => {
    window.scrollTo({ top: 0, behavior: "smooth" });
  });
  resultado.scrollIntoView({ behavior: "smooth" });
}

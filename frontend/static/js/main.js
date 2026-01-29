function renderResult(data) {
    const badgeClass =
        data.automation_potential === "high" ? "bg-danger" :
            data.automation_potential === "medium" ? "bg-warning text-dark" :
                "bg-success";
    return `
    <div class="card">
        <div class="card-body">
            <h5 class="card-title">Resultado del análisis</h5>
            <p>
                <strong>¿Es repetitivo?</strong>
                ${data.is_repetitive ? "Sí" : "No"}
            </p>
            <p>
                <strong>Potencial de automatización:</strong>
                ${data.automation_potential}
            </p>
            <p>
                <strong>Justificación:</strong><br>
                ${data.justification}
            </p>
            <span class="badge ${badgeClass}">
                ${data.automation_potential}
            </span>

        </div>
    </div>`;
}

async function analyzeText() {
    const text = document.getElementById("textInput").value;
    const loading = document.getElementById("loading");
    const result = document.getElementById("result");

    if (!text.trim()) {
        alert("Por favor, ingresa una descripción del proceso.");
        return;
    }

    loading.classList.remove("d-none");
    result.textContent = "";

    const response = await fetch("/analyze", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text, source: "ui" })
    });

    const data = await response.json();

    loading.classList.add("d-none");
    result.innerHTML = renderResult(data);

}
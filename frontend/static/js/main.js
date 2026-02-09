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

function renderExcelResults(data) {
    let rows = "";

    data.results.forEach((item, index) => {
        const badgeClass =
            item.automation_potential === "high" ? "bg-danger" :
            item.automation_potential === "medium" ? "bg-warning text-dark" :
            "bg-success";

        rows += `
        <tr>
            <td>${index + 1}</td>
            <td>${item.is_repetitive ? "Sí" : "No"}</td>
            <td>
                <span class="badge ${badgeClass}">
                    ${item.automation_potential}
                </span>
            </td>
            <td>${item.justification}</td>
        </tr>`;
    });

    return `
    <h5>Resultados (${data.total_rows} procesos)</h5>
    <div class="table-responsive">
        <table class="table table-bordered table-striped">
            <thead class="table-light">
                <tr>
                    <th>#</th>
                    <th>¿Repetitivo?</th>
                    <th>Automatización</th>
                    <th>Justificación</th>
                </tr>
            </thead>
            <tbody>
                ${rows}
            </tbody>
        </table>
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

async function analyzeExcel() {
    const fileInput = document.getElementById("excelFile");
    const loading = document.getElementById("excelLoading");
    const result = document.getElementById("excelResult");

    if (!fileInput.files.length) {
        alert("Por favor, selecciona un archivo Excel.");
        return;
    }

    const formData = new FormData();
    formData.append("file", fileInput.files[0]);

    loading.classList.remove("d-none");
    result.innerHTML = "";

     const response = await fetch("/analyze/excel", {
        method: "POST",
        body: formData
    });

    const data = await response.json();

    loading.classList.add("d-none");
    result.innerHTML = renderExcelResults(data);
}


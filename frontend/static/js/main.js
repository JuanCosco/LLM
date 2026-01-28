async function analyzeText() {
    const text = document.getElementById("textInput").value;

    const response = await fetch("/analyze", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            text: text,
            source: "ui"
        })
    });

    const data = await response.json();
    document.getElementById("result").textContent =
         JSON.stringify(data, null, 2);
    
}
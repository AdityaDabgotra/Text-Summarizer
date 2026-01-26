const btn = document.getElementById("summarizeBtn");
const inputText = document.getElementById("inputText");
const outputText = document.getElementById("outputText");
const loader = document.getElementById("loader");

btn.addEventListener("click", async () => {
    const text = inputText.value.trim();

    if (!text) {
        alert("Please enter some text!");
        return;
    }

    loader.style.display = "block";
    outputText.textContent = "";

    try {
        const response = await fetch("http://localhost:8080/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ "text":text })
        });

        const data = await response.json();

        if (data.summary) {
            outputText.textContent = data.summary;
        } else {
            outputText.textContent = "Something went wrong.";
        }
    } catch (error) {
        outputText.textContent = `${error}`;
    } finally {
        loader.style.display = "none";
    }
});

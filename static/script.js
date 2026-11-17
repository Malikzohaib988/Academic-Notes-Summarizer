const form = document.getElementById("analyzer-form");
const notesInput = document.getElementById("notes");
const taskInput = document.getElementById("task");
const analyzeButton = document.getElementById("analyze-button");
const statusMessage = document.getElementById("status");
const resultBox = document.getElementById("result");
const charCount = document.getElementById("char-count");
const copyButton = document.getElementById("copy-button");

notesInput.addEventListener("input", () => {
    charCount.textContent = notesInput.value.length.toLocaleString();
});

copyButton.addEventListener("click", async () => {
    try {
        await navigator.clipboard.writeText(resultBox.textContent);
        statusMessage.textContent = "Result copied to clipboard.";
    } catch {
        statusMessage.textContent = "Could not copy automatically. Please select and copy the result.";
    }
});

form.addEventListener("submit", async (event) => {
    event.preventDefault();

    const notes = notesInput.value.trim();
    const task = taskInput.value;

    if (!notes) {
        statusMessage.textContent = "Please paste your study notes first.";
        return;
    }

    statusMessage.textContent = "Analyzing your notes. Please wait...";
    resultBox.textContent = "";
    copyButton.disabled = true;
    analyzeButton.disabled = true;
    analyzeButton.textContent = "Working...";

    try {
        const response = await fetch("/analyze", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({notes, task})
        });

        const data = await response.json();
        if (!response.ok) {
            throw new Error(data.error || "The request could not be completed.");
        }

        resultBox.textContent = data.result;
        copyButton.disabled = false;
        statusMessage.textContent = "Done! Your result is ready.";
    } catch (error) {
        statusMessage.textContent = error.message;
        resultBox.textContent = "No result was returned. Check the message above.";
    } finally {
        analyzeButton.disabled = false;
        analyzeButton.textContent = "Analyze Notes";
    }
});

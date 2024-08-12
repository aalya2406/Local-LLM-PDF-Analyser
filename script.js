async function analyzePDF() {
    const pdfInput = document.getElementById("pdfInput").files[0];
    const question = document.getElementById("question").value;
    const loader = document.getElementById("loader");
    const answerDiv = document.getElementById("answer");

    // Show the loader
    loader.classList.remove("hidden");
    answerDiv.innerText = "";

    const formData = new FormData();
    formData.append("file", pdfInput);
    formData.append("question", question);

    const response = await fetch("/analyze", {
        method: "POST",
        body: formData
    });

    const data = await response.json();

    // Hide the loader
    loader.classList.add("hidden");

    answerDiv.innerText = data.answer;
}

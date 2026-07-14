const questionInput = document.getElementById("questionInput");
const sendBtn = document.getElementById("sendBtn");
const responseText = document.getElementById("responseText");

const answers = {
    tree: "A Binary Search Tree (BST) is a binary tree where every left child contains a smaller value and every right child contains a larger value.",
    dbms: "DBMS is software that stores, retrieves and manages data efficiently.",
    os: "An Operating System manages hardware, memory, files and processes.",
    network: "Computer Networks connect devices to share data using communication protocols.",
    ai: "Artificial Intelligence enables computers to perform tasks that normally require human intelligence."
};

function askQuestion() {

    const question = questionInput.value.trim();

    if (question === "") {
        alert("Please enter a question.");
        return;
    }

    responseText.innerHTML = "<em>Thinking...</em>";

    setTimeout(() => {

        const q = question.toLowerCase();

        let reply = "Sorry, I don't know that yet. Once the FastAPI backend is connected, I'll answer using the AI Tutor.";

        if (q.includes("tree"))
            reply = answers.tree;

        else if (q.includes("dbms"))
            reply = answers.dbms;

        else if (q.includes("operating") || q.includes("os"))
            reply = answers.os;

        else if (q.includes("network"))
            reply = answers.network;

        else if (q.includes("ai"))
            reply = answers.ai;

        responseText.textContent = reply;

    }, 800);

    questionInput.value = "";
}

sendBtn.addEventListener("click", askQuestion);

questionInput.addEventListener("keypress", function(e) {
    if (e.key === "Enter") {
        askQuestion();
    }
});
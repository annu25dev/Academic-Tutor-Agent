// ======================================
// EduPilot Dashboard
// ======================================

const BACKEND_URL = "";

const questionInput = document.getElementById("questionInput");
const sendBtn = document.getElementById("sendBtn");
const responseText = document.getElementById("responseText");

// ======================================
// Student Details
// ======================================

const studentId = localStorage.getItem("student_id");
const sessionId = localStorage.getItem("session_id");

const profile = JSON.parse(
    localStorage.getItem("studentProfile")
);

if (profile) {

    document.querySelector(".top-bar h1").innerHTML =
        `Hello, ${profile.name} 👋`;

}

// ======================================
// Ask Question
// ======================================

async function askQuestion() {

    console.log("1");

    const question = questionInput.value.trim();

    console.log("2");

    if (question === "") {

        alert("Please enter a question.");
        return;

    }

    console.log("3");

    if (!studentId || !sessionId) {

        alert("Session expired.");
        window.location.href = "form.html";
        return;

    }

    console.log("4");

    sendBtn.disabled = true;

    console.log("5");

    responseText.innerHTML =
        "<em>AI Teacher is thinking...</em>";

    console.log("6");

    try {
        console.log("7");

        const response = await fetch(
            `${BACKEND_URL}/api/chat`,
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({

                    student_id: studentId,
                    session_id: sessionId,
                    question: question

                })

            }
        );

        console.log("8");

        const result = await response.json();

        console.log("9");

        console.log("Backend Response:", result);

        if (!response.ok) {

            throw new Error(result.detail || "Backend Error");

        }

        // ======================================
        // Extract response safely
        // ======================================

        let aiAnswer = "";

        if (typeof result === "string") {

            aiAnswer = result;

        }

        else if (result.response) {

            aiAnswer = result.response;

        }

        else if (result.message) {

            aiAnswer = result.message;

        }

        else if (result.result) {

            aiAnswer = result.result;

        }

        else if (result.data) {

            aiAnswer = result.data;

        }

        else {

            aiAnswer = JSON.stringify(result, null, 2);

        }

        responseText.innerHTML = marked.parse(aiAnswer, {
               breaks: true
});

    }

    catch (error) {

        console.error(error);

        responseText.innerHTML =
            "<span style='color:#ff7b7b'>Unable to connect to backend.</span>";

    }

    finally {

        sendBtn.disabled = false;

        questionInput.value = "";

    }

}

// ======================================
// Events
// ======================================

sendBtn.addEventListener("click", askQuestion);

questionInput.addEventListener("keypress", function (event) {

    if (event.key === "Enter") {

        askQuestion();

    }

});
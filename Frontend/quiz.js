// =============================
// EduPilot Quiz Library
// =============================

// Search bar
const searchInput = document.querySelector(".search-box input");

// All quiz cards
const quizCards = document.querySelectorAll(".quiz-card");

// All Practice buttons
const practiceButtons = document.querySelectorAll(".practice-btn");


// -----------------------------
// Search Topics
// -----------------------------
searchInput.addEventListener("keyup", function () {

    const searchText = searchInput.value.toLowerCase();

    quizCards.forEach(function(card){

        const topic = card.querySelector("h2").textContent.toLowerCase();

        if(topic.includes(searchText)){
            card.style.display = "block";
        }
        else{
            card.style.display = "none";
        }

    });

});


// -----------------------------
// Practice Button
// -----------------------------
practiceButtons.forEach(function(button){

    button.addEventListener("click", function(e){

        e.preventDefault();

        const topic = this.parentElement.querySelector("h2").textContent;

        alert("Starting quiz for: " + topic);

        // Later this will become:
        // fetch("http://127.0.0.1:8000/quiz")

    });

});
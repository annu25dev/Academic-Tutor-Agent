// ================= Learning Level Slider =================

const levelSlider = document.getElementById("level");
const levelText = document.getElementById("levelText");

const levels = {
    1: "Beginner",
    2: "Intermediate",
    3: "Advanced"
};

levelSlider.addEventListener("input", function () {
    levelText.textContent = levels[this.value];
});


// ================= Form Submission =================

const profileForm = document.getElementById("profileForm");

profileForm.addEventListener("submit", function(event) {

    event.preventDefault(); // prevents page refresh

    // Collect form data
    const profileData = {

        name: document.getElementById("name").value,

        email: document.getElementById("email").value,

        college: document.getElementById("college").value,

        course: document.getElementById("course").value,

        semester: document.getElementById("semester").value,

        goal: document.getElementById("goal").value,

        learningStyle: document.querySelector(
            'input[name="style"]:checked'
        )?.value || "Not selected",

        subjects: document.getElementById("subjects").value,

        learningLevel: levels[levelSlider.value],

        about: document.getElementById("about").value
    };


    // Display data in console
    console.log("Student Profile:", profileData);


    // Save temporarily in browser storage
    localStorage.setItem(
        "studentProfile",
        JSON.stringify(profileData)
    );


    // Success message
    alert("Profile saved successfully! EduPilot will personalize your learning experience.");


    // Optional: move to next page
    // window.location.href = "dashboard.html";

});


// ================= Load Previous Data =================

window.addEventListener("load", function(){

    const savedProfile = localStorage.getItem("studentProfile");

    if(savedProfile){

        const data = JSON.parse(savedProfile);

        document.getElementById("name").value = data.name || "";
        document.getElementById("email").value = data.email || "";
        document.getElementById("college").value = data.college || "";
        document.getElementById("course").value = data.course || "";
        document.getElementById("semester").value = data.semester || "";
        document.getElementById("goal").value = data.goal || "";
        document.getElementById("subjects").value = data.subjects || "";
        document.getElementById("about").value = data.about || "";

        levelText.textContent = data.learningLevel || "Intermediate";

        const styleRadio = document.querySelector(
            `input[name="style"][value="${data.learningStyle}"]`
        );

        if(styleRadio){
            styleRadio.checked = true;
        }

    }

});
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

profileForm.addEventListener("submit", async function(event) {

    event.preventDefault();

    const profileData = {

        name: document.getElementById("name").value,

        school: "",

        stream: "",

        college: document.getElementById("college").value,

        college_degree: document.getElementById("course").value,

        specification: document.getElementById("subjects").value,

        learning_level: levels[levelSlider.value],

        class_name: "",

        year: document.getElementById("semester").value
    };

    try{

        const response = await fetch("http://127.0.0.1:8000/api/register",{

            method:"POST",

            headers:{
                "Content-Type":"application/json"
            },

            body:JSON.stringify(profileData)

        });

        const result = await response.json();

        console.log(result);

        if(result.status==="success"){

          // Save student id
localStorage.setItem(
    "student_id",
    result.student_id
);

// Save profile
localStorage.setItem(
    "studentProfile",
    JSON.stringify(profileData)
);

// =======================
// Create first chat session
// =======================

const chatResponse = await fetch(
    `http://127.0.0.1:8000/api/new-chat?student_id=${result.student_id}`,
    {
        method: "POST"
    }
);

const chatResult = await chatResponse.json();

console.log(chatResult);

// Save session id
localStorage.setItem(
    "session_id",
    chatResult.session_id
);

alert("Registration Successful!");

window.location.href = "/dashboard";
        }

        else{

            alert("Registration Failed");

        }

    }

    catch(error){

        console.error(error);

        alert("Cannot connect to backend.");

    }

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
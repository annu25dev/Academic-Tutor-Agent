// ==============================
// EduPilot - Notes Page
// ==============================


// ==============================
// Elements
// ==============================

const fileInput = document.getElementById("fileUpload");

const fileName = document.getElementById("selectedFile");

const subject = document.getElementById("subject");

const topic = document.getElementById("topic");

const semester = document.getElementById("semester");

const uploadButton = document.getElementById("uploadButton");

const uploadBox = document.querySelector(".upload-box");

const recentUploads = document.getElementById("recentUploads");



// ==============================
// Show Selected File
// ==============================

fileInput.addEventListener("change", function () {


    if(this.files.length > 0){

        fileName.textContent = this.files[0].name;

    }

    else{

        fileName.textContent = "No file selected";

    }


});





// ==============================
// Drag & Drop
// ==============================


uploadBox.addEventListener("dragover", function(e){


    e.preventDefault();


    uploadBox.style.borderColor="#8B5CF6";


});




uploadBox.addEventListener("dragleave", function(){


    uploadBox.style.borderColor="#D183C9";


});




uploadBox.addEventListener("drop", function(e){


    e.preventDefault();


    uploadBox.style.borderColor="#D183C9";



    if(e.dataTransfer.files.length > 0){


        fileInput.files = e.dataTransfer.files;


        fileName.textContent =
        e.dataTransfer.files[0].name;


    }


});






// ==============================
// Upload Button
// ==============================


uploadButton.addEventListener("click", function(){



    // Validate File

    if(fileInput.files.length === 0){


        alert("Please choose a file.");

        return;


    }



    // Validate Subject

    if(subject.value.trim() === ""){


        alert("Enter Subject.");

        return;


    }




    // Validate Topic

    if(topic.value.trim() === ""){


        alert("Enter Topic.");

        return;


    }




    // Validate Semester

    if(semester.value === ""){


        alert("Select Semester/Class.");

        return;


    }





    const file = fileInput.files[0];



    let icon="fa-file";



    if(file.name.toLowerCase().endsWith(".pdf")){


        icon="fa-file-pdf";


    }


    else if(

        file.name.toLowerCase().endsWith(".doc") ||

        file.name.toLowerCase().endsWith(".docx")

    ){


        icon="fa-file-word";


    }


    else if(file.name.toLowerCase().endsWith(".txt")){


        icon="fa-file-lines";


    }






    // Create Upload Card


    const card=document.createElement("div");


    card.className="file-card";



    card.innerHTML=`

        <i class="fa-solid ${icon}"></i>

        <span>${file.name}</span>

    `;





    // Add newest upload on top

    recentUploads.prepend(card);




    alert("Notes uploaded successfully!");





    // ==============================
    // Reset Form
    // ==============================


    fileInput.value="";


    fileName.textContent="No file selected";


    subject.value="";


    topic.value="";


    semester.selectedIndex=0;



});
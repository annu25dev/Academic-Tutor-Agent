// ==============================
// EduPilot - Notes Page
// ==============================

const BACKEND_URL = "";

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

    if (this.files.length > 0) {
        fileName.textContent = this.files[0].name;
    } else {
        fileName.textContent = "No file selected";
    }

});

// ==============================
// Drag & Drop
// ==============================

uploadBox.addEventListener("dragover", function (e) {

    e.preventDefault();
    uploadBox.style.borderColor = "#8B5CF6";

});

uploadBox.addEventListener("dragleave", function () {

    uploadBox.style.borderColor = "#D183C9";

});

uploadBox.addEventListener("drop", function (e) {

    e.preventDefault();

    uploadBox.style.borderColor = "#D183C9";

    if (e.dataTransfer.files.length > 0) {

        fileInput.files = e.dataTransfer.files;
        fileName.textContent = e.dataTransfer.files[0].name;

    }

});

// ==============================
// Load Recent Uploads
// ==============================

async function loadRecentUploads() {

    try {

        const response = await fetch(`${BACKEND_URL}/api/documents`);

        const result = await response.json();

        if (result.status === "success") {

            recentUploads.innerHTML = "";

            result.documents.forEach(file => {

                let icon = "fa-file";

                if (file.toLowerCase().endsWith(".pdf")) {
                    icon = "fa-file-pdf";
                }
                else if (
                    file.toLowerCase().endsWith(".doc") ||
                    file.toLowerCase().endsWith(".docx")
                ) {
                    icon = "fa-file-word";
                }
                else if (file.toLowerCase().endsWith(".txt")) {
                    icon = "fa-file-lines";
                }

                const card = document.createElement("div");

                card.className = "file-card";

                card.innerHTML = `
                    <i class="fa-solid ${icon}"></i>
                    <span>${file}</span>
                `;

                recentUploads.appendChild(card);

            });

        }

    }

    catch (error) {

        console.error("Unable to load uploaded files", error);

    }

}

// ==============================
// Upload Button
// ==============================

uploadButton.addEventListener("click", async function () {

    // Validation

    if (fileInput.files.length === 0) {

        alert("Please choose a file.");
        return;

    }

    if (subject.value.trim() === "") {

        alert("Enter Subject.");
        return;

    }

    if (topic.value.trim() === "") {

        alert("Enter Topic.");
        return;

    }

    if (semester.value === "") {

        alert("Select Semester/Class.");
        return;

    }

    const file = fileInput.files[0];

    const formData = new FormData();

    formData.append("file", file);

    try {

        uploadButton.disabled = true;

        uploadButton.innerHTML = `
            <i class="fa-solid fa-spinner fa-spin"></i>
            Uploading...
        `;

        const response = await fetch(

            `${BACKEND_URL}/api/upload`,

            {
                method: "POST",
                body: formData
            }

        );

        const result = await response.json();

        if (result.status === "success") {

            uploadButton.innerHTML = `
                <i class="fa-solid fa-circle-check"></i>
                Uploaded Successfully
            `;

            // Refresh uploads
            loadRecentUploads();

            // Reset form

            fileInput.value = "";
            fileName.textContent = "No file selected";
            subject.value = "";
            topic.value = "";
            semester.selectedIndex = 0;

            // Restore button after 2 sec

            setTimeout(() => {

                uploadButton.innerHTML = `
                    <i class="fa-solid fa-upload"></i>
                    Upload Notes
                `;

            }, 2000);

        }

        else {

            alert("Upload failed.");

            uploadButton.innerHTML = `
                <i class="fa-solid fa-upload"></i>
                Upload Notes
            `;

        }

    }

    catch (error) {

        console.error(error);

        alert("Cannot connect to backend.");

        uploadButton.innerHTML = `
            <i class="fa-solid fa-upload"></i>
            Upload Notes
        `;

    }

    finally {

        uploadButton.disabled = false;

    }

});

// ==============================
// Initial Load
// ==============================

loadRecentUploads();
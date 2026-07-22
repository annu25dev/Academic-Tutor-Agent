// =======================================
// EduPilot Study Planner
// =======================================

const BACKEND_URL = "";

const planContainer = document.getElementById("planContainer");

const studentId = localStorage.getItem("student_id");


// =======================================
// Load Saved Plans
// =======================================

async function loadPlans() {

    if (!studentId) {

        planContainer.innerHTML = `
            <div class="empty-state">
                <i class="fa-solid fa-book-open"></i>
                <p>No student found.</p>
            </div>
        `;

        return;
    }

    try {

        const response = await fetch(
            `${BACKEND_URL}/api/plans/${studentId}`
        );

        const result = await response.json();

        if (
            result.status === "success" &&
            result.plans.length > 0
        ) {

            displayPlans(result.plans);

        }

        else {

            planContainer.innerHTML = `
                <div class="empty-state">
                    <i class="fa-solid fa-book-open"></i>
                    <p>No study plans available.</p>
                </div>
            `;

        }

    }

    catch (error) {

        console.error(error);

        planContainer.innerHTML = `
            <div class="empty-state">
                <i class="fa-solid fa-circle-exclamation"></i>
                <p>Cannot connect to backend.</p>
            </div>
        `;

    }

}


// =======================================
// Display Plans
// =======================================

function displayPlans(plans) {

    planContainer.innerHTML = "";

    plans.forEach(plan => {

        const card = document.createElement("div");

        card.className = "plan-card";

        card.innerHTML = `

            <i class="fa-solid fa-calendar-check"></i>

            <div style="width:100%;">

                <h3>${plan.topic}</h3>

                <p>
                    Created :
                    ${plan.timestamp}
                </p>

                <br>

                <button
                    class="viewPlanBtn"
                    data-plan="${encodeURIComponent(plan.plan)}">

                    View Study Plan

                </button>

            </div>

        `;

        planContainer.appendChild(card);

    });


    document.querySelectorAll(".viewPlanBtn").forEach(button => {

        button.addEventListener("click", function () {

            const plan = decodeURIComponent(
                this.dataset.plan
            );

            showPlan(plan);

        });

    });

}


// =======================================
// Show Complete Plan
// =======================================

function showPlan(plan) {

    const newWindow = window.open("", "_blank");

    newWindow.document.write(`

        <html>

        <head>

        <title>Study Plan</title>

        <style>

        body{

            font-family:Arial;

            background:#020617;

            color:white;

            padding:40px;

            line-height:1.8;

        }

        h1{

            color:#D183C9;

        }

        pre{

            white-space:pre-wrap;

            font-size:16px;

        }

        </style>

        </head>

        <body>

            <h1>Study Plan</h1>

            <pre>${plan}</pre>

        </body>

        </html>

    `);

}


// =======================================
// Initial Load
// =======================================

loadPlans();
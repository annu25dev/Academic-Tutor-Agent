// =============================
// EduPilot Study Planner
// =============================


const generateBtn =
document.getElementById("generateBtn");


const planContainer =
document.getElementById("planContainer");




// Generate Plan


generateBtn.addEventListener(
"click",
function(){



const subject =
document.getElementById("subject").value;


const topic =
document.getElementById("topic").value;


const date =
document.getElementById("examDate").value;


const hours =
document.getElementById("hours").value;




if(subject=="" || topic==""){

alert("Please fill subject and topic");

return;

}




createPlan(
subject,
topic,
date,
hours
);



});






// Create Study Cards


function createPlan(
subject,
topic,
date,
hours
){



planContainer.innerHTML="";



const plans=[


"Understand basic concepts",

"Practice important questions",

"Revise previous notes",

"Take a self assessment quiz"


];



plans.forEach(
(task,index)=>{


const card =
document.createElement("div");


card.className="plan-card";


card.innerHTML=`

<i class="fa-solid fa-calendar-check"></i>


<div>

<h3>
Day ${index+1}: ${task}
</h3>


<p>
${subject} - ${topic}
<br>
Study Time: ${hours} hours/day
</p>


</div>

`;



planContainer.appendChild(card);



});


}
// =======================================
// EduPilot Quiz Library
// =======================================


const BACKEND_URL = "";


const studentId = localStorage.getItem("student_id");


const quizGrid = document.getElementById("quizGrid");


let quizzes=[];





// =======================================
// Load Saved Quizzes
// =======================================


async function loadQuizzes(){


if(!studentId){


quizGrid.innerHTML=`

<div class="empty-state">

<i class="fa-solid fa-user"></i>

<p>
No student found.
</p>

</div>

`;


return;

}



try{


const response = await fetch(

`${BACKEND_URL}/api/quizzes/${studentId}`

);



const result = await response.json();



console.log(result);




if(

result.status==="success" &&

result.quizzes.length>0

){


quizzes=result.quizzes;


displayQuizzes(quizzes);


}



else{


quizGrid.innerHTML=`

<div class="empty-state">

<i class="fa-solid fa-circle-question"></i>

<p>
No quizzes available.
</p>

</div>

`;

}


}



catch(error){


console.error(error);


quizGrid.innerHTML=`

<div class="empty-state">

<i class="fa-solid fa-triangle-exclamation"></i>

<p>
Cannot connect to backend.
</p>

</div>

`;

}


}








// =======================================
// Display Quiz Cards
// =======================================


function displayQuizzes(list){


quizGrid.innerHTML="";



list.forEach((quiz)=>{


const card=document.createElement("div");


card.className="quiz-card";



card.innerHTML=`

<i class="fa-solid fa-circle-question"></i>


<h2>

${quiz.topic}

</h2>



<p>

Generated :

<br>

${quiz.timestamp}

</p>



<button

class="practice-btn"

data-quiz="${encodeURIComponent(quiz.quiz)}"

>


Practice Now


</button>


`;



quizGrid.appendChild(card);



});



attachButtonEvents();


}








// =======================================
// Show Complete Quiz
// =======================================


function showQuiz(quiz){



const newWindow = window.open("", "_blank");



newWindow.document.write(`


<html>


<head>


<title>AI Generated Quiz</title>


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

text-align:center;

}


.quiz-box{

background:#0a0f1f;

border:2px solid #2a3246;

border-radius:15px;

padding:25px;

}


pre{

white-space:pre-wrap;

font-size:16px;

}



</style>


</head>



<body>


<h1>

EduPilot AI Quiz

</h1>



<div class="quiz-box">


<pre>

${quiz}

</pre>


</div>



</body>


</html>



`);



}









// =======================================
// Button Events
// =======================================


function attachButtonEvents(){



document.querySelectorAll(".practice-btn")

.forEach(button=>{


button.addEventListener("click",function(){



const quiz = decodeURIComponent(

this.dataset.quiz

);



showQuiz(quiz);



});



});


}







// =======================================
// Initial Load
// =======================================


loadQuizzes();
// ===============================
// EduPilot Chat History JS
// ===============================


const BACKEND_URL = "";


const historyContainer =
document.getElementById("historyContainer");


const studentId =
localStorage.getItem("student_id");




// ===============================
// Fetch Chat Sessions
// ===============================


async function fetchChatHistory(){


if(!studentId){


historyContainer.innerHTML=`

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

`${BACKEND_URL}/api/chat-sessions/${studentId}`

);



const result = await response.json();



console.log(result);



if(

result.status==="success"

){


displayHistory(result.sessions);


}

else{


showEmpty();

}


}



catch(error){


console.error(error);


historyContainer.innerHTML=`

<div class="empty-state">

<i class="fa-solid fa-triangle-exclamation"></i>

<p>
Unable to connect to backend.
</p>

</div>

`;

}



}








// ===============================
// Display Sessions
// ===============================


function displayHistory(sessions){


historyContainer.innerHTML="";



if(sessions.length===0){


showEmpty();

return;


}



sessions.forEach((sessionId,index)=>{


const card=document.createElement("div");


card.className="history-card";



card.innerHTML=`

<i class="fa-solid fa-comments"></i>


<div>


<h3>

Chat Session ${index+1}

</h3>


<p>

${sessionId}

</p>


</div>


`;



card.addEventListener("click",()=>{


openChat(sessionId);


});



historyContainer.appendChild(card);



});


}







// ===============================
// Empty State
// ===============================


function showEmpty(){


historyContainer.innerHTML=`

<div class="empty-state">

<i class="fa-solid fa-comments"></i>

<p>
No previous chats found.
</p>

</div>

`;

}







// ===============================
// Open Chat
// ===============================


async function openChat(sessionId){


try{


const response=await fetch(

`${BACKEND_URL}/api/chat/${studentId}/${sessionId}`

);



const result=await response.json();



console.log(result);



if(result.status==="success"){


showConversation(result.conversation);


}

else{


alert("Unable to load chat.");

}


}



catch(error){


console.error(error);


alert("Cannot connect to backend.");

}



}








// ===============================
// Show Conversation
// ===============================


function showConversation(conversation){


const newWindow = window.open("", "_blank");



let chatHTML="";



conversation.forEach(msg=>{


let roleClass =
msg.role==="user"
?
"user-msg"
:
"ai-msg";



chatHTML+=`


<div class="chat-message ${roleClass}">


<h3>

${msg.role.toUpperCase()}

</h3>



<p>

${msg.content}

</p>


</div>


`;


});






newWindow.document.write(`


<html>


<head>


<title>
EduPilot Chat
</title>



<style>


body{

font-family:Arial;

background:#020617;

color:white;

padding:40px;

line-height:1.7;

}



h1{

text-align:center;

color:#D183C9;

margin-bottom:30px;

}



.chat-message{

background:#0a0f1f;

border:2px solid #2a3246;

border-radius:15px;

padding:20px;

margin-bottom:20px;

}



.user-msg{

border-left:5px solid #8B5CF6;

}



.ai-msg{

border-left:5px solid #D183C9;

}



h3{

margin-bottom:10px;

color:#D183C9;

}



p{

white-space:pre-wrap;

}


</style>


</head>




<body>


<h1>
EduPilot Chat Conversation
</h1>


${chatHTML}



</body>


</html>


`);



}






// ===============================
// Load
// ===============================


fetchChatHistory();
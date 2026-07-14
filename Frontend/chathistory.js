// ===============================
// EduPilot Chat History JS
// ===============================


// Select container where chats will appear

const historyContainer = document.getElementById(
    "historyContainer"
);




// Temporary chat data
// Later this will come from FastAPI

const chatHistory = [

    {
        id:1,
        title:"Binary Search Trees",
        date:"Yesterday • 8:45 PM"
    },


    {
        id:2,
        title:"Operating Systems Notes",
        date:"2 Days Ago"
    },


    {
        id:3,
        title:"Dynamic Programming",
        date:"Last Week"
    },


    {
        id:4,
        title:"Computer Networks",
        date:"Last Week"
    },


    {
        id:5,
        title:"DBMS Revision",
        date:"Last Month"
    }

];





// ===============================
// Display Chat History
// ===============================


function displayHistory(){


    historyContainer.innerHTML = "";



    chatHistory.forEach(chat => {



        const card = document.createElement("div");


        card.classList.add("history-card");



        card.innerHTML = `

            <i class="fa-solid fa-comments"></i>


            <div>

                <h3>${chat.title}</h3>

                <p>${chat.date}</p>

            </div>

        `;



        // When user clicks a chat

        card.addEventListener(
            "click",
            function(){

                openChat(chat.id);

            }
        );



        historyContainer.appendChild(card);



    });


}






// ===============================
// Open Selected Chat
// ===============================


function openChat(chatId){


    console.log(
        "Opening chat:",
        chatId
    );


    /*
       Later connect this with:

       chat.html?id=chatId

       where complete conversation
       will be displayed.
    */


}






// ===============================
// Future FastAPI Connection
// ===============================


async function fetchChatHistory(){


    /*
    
    Later replace dummy data with:

    
    const response = await fetch(
        "http://127.0.0.1:8000/chat-history"
    );


    const data = await response.json();


    chatHistory = data;


    */


    displayHistory();


}






// Load page

fetchChatHistory();
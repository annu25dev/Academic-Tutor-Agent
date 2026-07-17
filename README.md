<div align="center">

<img src="Frontend/logo.jpg" width="170"/>

# 🎓 EduPilot

### Your AI-Powered Multi-Agent Academic Learning Assistant

*Personalized • Context-Aware • Retrieval-Augmented • CrewAI Powered*

---

Built using **CrewAI**, **FastAPI**, **Groq LLM**, **ChromaDB**, and **Retrieval-Augmented Generation (RAG)** to provide an intelligent, personalized, and interactive learning experience.

</div>

---

# 📚 About EduPilot

EduPilot is an AI-powered academic learning platform designed to provide personalized assistance to students through a collaborative **multi-agent architecture**.

Unlike traditional AI chatbots that generate a single generic response, EduPilot intelligently understands the student's intent, retrieves relevant academic resources, selects the appropriate AI agents, and combines their outputs into a unified response tailored to the student's learning needs.

The system is powered by **CrewAI**, where multiple specialized AI agents collaborate to solve different aspects of a student's query. Whether the student wants to understand a difficult concept, generate quizzes, prepare a study plan, assess their understanding, or ask questions from uploaded notes, EduPilot automatically activates the required agents behind the scenes.

To ensure continuity across conversations, EduPilot maintains a personalized memory for every student. Each learner is assigned a **unique Student ID**, through which the platform stores profile information, learning progress, generated quizzes, study plans, and previous interactions. Every conversation is further organized using a **Session ID**, allowing multiple chat sessions while preserving complete conversation history.

EduPilot also integrates **Retrieval-Augmented Generation (RAG)** to provide document-aware responses. Students can upload study materials such as PDFs, DOCX, PPTX, TXT, and Excel files. These documents are processed, embedded into a vector database using **ChromaDB**, and retrieved whenever relevant questions are asked, ensuring accurate and context-aware answers.

Together, personalization, persistent memory, intelligent routing, and document retrieval make EduPilot a complete AI-powered study companion rather than a traditional chatbot.

---

# ✨ Key Features

## 🎯 Personalized Learning

- Unique Student Profile
- Personalized learning history
- Persistent academic memory
- Individual study recommendations

---

## 🤖 Multi-Agent Intelligence

EduPilot combines multiple AI agents that collaborate together:

- Router Agent
- Tutor Agent
- Quiz Agent
- Study Planner Agent
- Assessment Agent
- Memory Agent
- Academic RAG Tool

Each agent specializes in a different educational task, enabling modular and scalable problem-solving.

---

## 📄 Document-Based Learning (RAG)

Students can upload:

- PDF
- DOCX
- PPTX
- TXT
- XLSX

The uploaded documents are converted into embeddings and stored in ChromaDB, allowing EduPilot to answer questions directly from the student's own study materials.

---

## 🧠 Intelligent Prompt Routing

EduPilot supports complex prompts containing multiple learning requests.

Example:

> "Teach me Lunar Eclipse and create a study plan for Web Development."

Instead of generating one generic response, EduPilot:

- Detects multiple intents
- Separates the query
- Routes each task to the appropriate AI agent
- Combines all outputs into a single response

---

## 💬 Persistent Chat History

Every conversation is automatically stored using unique Session IDs, allowing students to revisit previous discussions without losing context.

---

## 📝 AI Quiz Generation

Automatically creates personalized quizzes based on:

- Student profile
- Previous learning
- Uploaded study materials

---

## 📅 AI Study Planner

Generates customized study schedules based on:

- Student level
- Previous learning
- Exam goals
- Uploaded syllabus

---

## 📊 Assessment Agent

Evaluates the student's understanding through multiple assessment modes and provides structured feedback.

---

# 🏗️ System Architecture

```text
                         Student
                            │
                            ▼
                     Landing Page
                            │
                            ▼
                  Student Registration
                            │
                            ▼
                     Memory Agent
                     (Student Profile)
                            │
                            ▼
                     Router Agent
                            │
        ┌──────────┬──────────┬──────────┬──────────┐
        ▼          ▼          ▼          ▼
     Tutor      Planner     Quiz     Assessment
        │          │          │          │
        └──────────┴──────────┴──────────┘
                     │
                     ▼
               Academic RAG Tool
                     │
                     ▼
                 ChromaDB Vector DB
                     │
                     ▼
               Personalized Response
```

---

# ⚙️ EduPilot Workflow

```text
Student

        │

        ▼

Landing Page

        │

        ▼

Profile Creation

        │

        ▼

Student ID Generated

        │

        ▼

Memory Agent

        │

        ▼

Dashboard

        │

        ▼

Student submits a query

        │

        ▼

Router Agent analyses intent

        │

        ├───────────────► Document Required?

        │                     │

        │                     ▼

        │              Academic RAG Tool

        │                     │

        ▼                     ▼

Tutor Agent   Quiz Agent   Planner Agent   Assessment Agent

        │         │              │                │

        └─────────┴──────────────┴────────────────┘

                    ▼

          Final AI Response Generated

                    ▼

Conversation saved using Session ID

                    ▼

Displayed in Chat History
```

---

# 🧠 Memory Architecture

EduPilot maintains personalized learning through a JSON-based memory system.

## Student ID

Every new student is assigned a unique **Student ID** during registration.

The Student ID is used to store:

- Student Profile
- Previous Learning
- Saved Quizzes
- Saved Study Plans
- Academic Progress

This information is stored inside the Memory Agent as structured JSON files, enabling personalized responses across future interactions.

---

## Session ID

Whenever a student starts a new conversation, EduPilot generates a unique **Session ID**.

Each session stores:

- User queries
- AI responses
- Conversation timeline

This enables multiple independent chat sessions while preserving complete conversation history.

The combination of **Student ID** and **Session ID** allows EduPilot to deliver continuity, personalization, and long-term learning support.

---

# 📄 Retrieval-Augmented Generation (RAG)

EduPilot enhances response accuracy using a Retrieval-Augmented Generation pipeline.

Workflow:

```text
Upload Notes

      │

      ▼

FastAPI Upload Endpoint

      ▼

Document Ingestion Pipeline

      ▼

Text Chunking

      ▼

Embedding Generation

      ▼

ChromaDB Storage

      ▼

Semantic Retrieval

      ▼

Relevant Context Retrieved

      ▼

Academic RAG Tool

      ▼

Groq LLM

      ▼

Context-Aware Response
```

By combining semantic retrieval with Large Language Models, EduPilot minimizes hallucinations and produces responses grounded in the student's uploaded learning materials.
## ✨ Key Features

- 🤖 **Multi-Agent AI Architecture** powered by CrewAI.
- 🧠 **Router Agent** intelligently analyzes user queries and coordinates multiple AI agents for complex requests.
- 📚 **Academic Tutor Agent** provides personalized explanations using Retrieval-Augmented Generation (RAG).
- 📝 **Quiz Agent** automatically generates topic-based quizzes from uploaded study materials.
- 📅 **Study Planner Agent** creates personalized study roadmaps based on learning history and uploaded content.
- 📊 **Assessment Agent** evaluates student understanding through multiple assessment modes.
- 💾 **Persistent Memory System** stores student profiles, learning history, quizzes, study plans, and chat sessions using unique Student IDs and Session IDs.
- 📂 **Document Upload Support** for PDF, DOCX, PPTX, XLSX, and TXT files.
- 🔍 **Semantic Search** using ChromaDB and Hugging Face Sentence Transformers.
- 💬 **Chat History Management** with session-wise conversation retrieval.
- 📖 **Quiz Library** to revisit previously generated quizzes.
- 🗓️ **Study Planner Library** to access saved study plans anytime.
- 🌙 **Modern Responsive Frontend** with an intuitive dashboard and interactive UI.
  # 🏗️ System Architecture

EduPilot follows a modular **multi-agent architecture** built using **CrewAI**, where each agent is responsible for a specialized academic task. Instead of relying on a single AI model for every request, EduPilot intelligently distributes work among multiple collaborating agents to provide accurate, context-aware, and personalized responses.

The complete workflow is illustrated below.

```text
                           ┌──────────────────────┐
                           │      Student         │
                           └──────────┬───────────┘
                                      │
                                      ▼
                           Student Registration
                                      │
                                      ▼
                         Student ID Generation
                                      │
                                      ▼
                          Memory Agent (JSON)
                                      │
                 Stores Student Profile & Learning History
                                      │
                                      ▼
                               User Query
                                      │
                                      ▼
                              Router Agent
                                      │
      ┌──────────────────────┬──────────────┬────────────────────┐
      │                      │              │                    │
      ▼                      ▼              ▼                    ▼
Tutor Agent            Quiz Agent    Planner Agent    Assessment Agent
      │                      │              │                    │
      └───────────────┬──────┴──────────────┴────────────────────┘
                      │
                      ▼
             Academic RAG Tool (if required)
                      │
                      ▼
     ChromaDB + HuggingFace Embeddings + Uploaded Documents
                      │
                      ▼
              Context-Aware AI Response
                      │
                      ▼
         Chat History + Memory Updated (JSON)
```

---

# ⚙️ Workflow

### Step 1 — Student Registration

A new student first creates a profile through the registration page.

EduPilot automatically generates a **unique Student ID** for every learner. This ID acts as the primary identity throughout the platform and is used to retrieve the student's personalized information in future sessions.

---

### Step 2 — Memory Initialization

The Memory Agent creates a dedicated memory space for the student.

It stores:

- Student Profile
- Previous Learning History
- Generated Quizzes
- Generated Study Plans
- Chat Sessions

This enables EduPilot to remember the student's academic progress across multiple conversations.

---

### Step 3 — User Query

The student asks an academic question or uploads study material.

Examples:

- Teach me Binary Trees
- Generate quiz from these notes
- Make a study plan for DBMS
- Assess my understanding of Networking

---

### Step 4 — Intelligent Routing

The Router Agent is the central decision-making component of EduPilot.

It analyzes the student's prompt, detects the required intent(s), and activates only the relevant AI agents.

For multi-intent prompts, the Router Agent separates each request and forwards it to the correct agent while preserving the intended execution order.

Example:

> Teach me Lunar Eclipse and create a study plan for Web Development.

The Router Agent automatically routes:

- "Teach me Lunar Eclipse" → Tutor Agent
- "Create a study plan for Web Development" → Study Planner Agent

The outputs are then combined into a single coherent response.

---

### Step 5 — Academic RAG Retrieval

Whenever document-based knowledge is required, the selected agent invokes the Academic RAG Tool.

The RAG pipeline:

- Retrieves relevant document chunks from ChromaDB.
- Performs semantic similarity search.
- Supplies only the most relevant context to the LLM.

This ensures responses remain grounded in the uploaded study material rather than relying solely on the language model's general knowledge.

---

### Step 6 — Agent Execution

Depending on the Router Agent's decision, one or more specialized agents are executed.

**Tutor Agent**

- Explains academic concepts
- Uses uploaded documents whenever available

**Quiz Agent**

- Generates personalized quizzes
- Considers previous learning history

**Study Planner Agent**

- Creates structured study schedules
- Organizes topics into achievable timelines

**Assessment Agent**

- Evaluates learning through different assessment modes
- Provides structured feedback

---

### Step 7 — Personalized Memory Update

After generating the final response, EduPilot updates the student's memory automatically.

The system records:

- Newly learned topics
- Generated quizzes
- Study plans
- Updated learning history

This enables future recommendations to become increasingly personalized.

---

### Step 8 — Chat History Management

Every conversation is assigned a unique **Session ID**.

Each session stores:

- User prompts
- AI responses
- Conversation timeline

Students can revisit previous conversations through the Chat History module without losing context.
# 📂 Project Structure

```text
EduPilot
│
├── Backend
│   │
│   ├── Assessment_agent
│   │     ├── agent.py
│   │     └── task.py
│   │
│   ├── Chat_history
│   │     └── .gitkeep
│   │
│   ├── fastapi_app
│   │     └── main.py
│   │
│   ├── Memory_agent
│   │     ├── agent.py
│   │     ├── task.py
│   │     └── memory_service.py
│   │
│   ├── Planner_agent
│   │     ├── agent.py
│   │     └── task.py
│   │
│   ├── Quiz_agent
│   │     ├── agent.py
│   │     └── task.py
│   │
│   ├── RAG_agent
│   │     ├── ingestion_pipeline.py
│   │     ├── retrieval_pipeline.py
│   │     ├── rag_tool.py
│   │     ├── docs/
│   │     └── db/
│   │
│   ├── Router_agent
│   │     ├── agent.py
│   │     └── task.py
│   │
│   ├── Tutor_agent
│   │     ├── agent.py
│   │     └── task.py
│   │
│   ├── .env
│   ├── chat_history.py
│   ├── crew.py
│   ├── llm.py
│   └── Pydantic_models.py
│
├── Frontend
│   │
│   ├── agent.html
│   ├── agent.css
│   ├── agent.js
│   │
│   ├── form.html
│   ├── form.css
│   ├── form.js
│   │
│   ├── dashboard.html
│   ├── dashboard.css
│   ├── dashboard.js
│   │
│   ├── notes.html
│   ├── notes.css
│   ├── notes.js
│   │
│   ├── quiz.html
│   ├── quiz.css
│   ├── quiz.js
│   │
│   ├── studyplanner.html
│   ├── studyplanner.css
│   ├── studyplanner.js
│   │
│   ├── chathistory.html
│   ├── chathistory.css
│   └── chathistory.js
│
├── .gitignore
├── requirements.txt
├── Testing.md
└── README.md

# 📚 Technologies Used

- 🐍 Python
- ⚡ FastAPI
- 🤖 CrewAI
- 🧠 Groq Llama 3.3 70B (LiteLLM)
- 🔍 LangChain
- 📦 ChromaDB
- 🤗 HuggingFace Sentence Transformers
- 📄 Pydantic
- 🌐 HTML5
- 🎨 CSS3
- ⚙️ JavaScript
- 📂 JSON
- 🔀 Git & GitHub
- 🧪 Swagger UI

# 📸 Application Screenshots

## 🏠 Landing Page
![Landing Page](Screenshots/Landing page.png)

## 💬 Main Interface
![Main Interface](Screenshots/Main-interface.png)

## 📂 Upload Notes
![Upload](Screenshots/Upload file interface.png)

## 🧠 Chat History
![History](Screenshots/Chat history.png)

## 📜 Chat Conversation
![Chat](Screenshots/Chat Conversation.png)

## 📝 Quiz Library
![Quiz](Screenshots/quiz.png)

## 📅 Study Planner
![Planner](Screenshots/Studyplanner.png)

## 🤖 Saved Study Plans
![AI Planner](Screenshots/AI planner.png)

## 📚 Saved Quizzes
![AI Quiz](Screenshots/AI quiz.png)

# 👥 Team Contributions

EduPilot was developed collaboratively by a team of five members, with each member contributing to different modules of the project, including AI agent development, backend services, frontend development, Retrieval-Augmented Generation (RAG), memory management, testing, and system integration.

---
## 👩‍💻 Member 1 – <ANNU TIWARI>

### 🧠 AI Workflow, Routing & Backend Integration

- 🧭 Designed and developed the **Router Agent**, which serves as the central decision-making component of EduPilot by analyzing user prompts, handling multi-intent queries, and routing tasks to the appropriate AI agents in the correct execution order.
- 📝 Developed the **Assessment Agent** using CrewAI, defining its role, prompts, and structured evaluation modes to assess students through multiple assessment strategies.
- ⚙️ Built the central **CrewAI workflow (`crew.py`)**, integrating all AI agents, implementing RAG initialization after document uploads, and enabling personalized execution using Student ID and Session ID.
- 🚀 Developed several **FastAPI endpoints** including student registration, chat session creation, conversation retrieval, uploaded document listing, saved quiz retrieval, and study plan retrieval.
- 🌐 Integrated backend APIs with the frontend for **Chat History**, **Quiz Library**, **Study Planner**, and uploaded document management while configuring the project with **Groq Llama 3.3 70B Versatile** through LiteLLM.

---

## 👩‍💻 Member 2 – <ISHITA SANGER>

### 🧠 Memory Agent, RAG Pipeline & Data Management

- 💾 Designed and implemented the **Memory Agent**, providing persistent student memory using JSON-based storage with unique Student IDs and Session IDs for personalized learning across conversations.
- 📚 Built the complete **Text-based Retrieval-Augmented Generation (RAG) pipeline**, supporting multiple document formats including PDF, DOCX, PPTX, XLSX, and TXT using LangChain, ChromaDB, and Hugging Face Sentence Transformers.
- 🔍 Developed document ingestion, chunking, embedding generation, semantic retrieval, and optimized retrieval parameters for efficient document-grounded responses.
- 💬 Implemented the **Chat History module**, enabling session-wise storage and retrieval of conversations while maintaining continuity across multiple interactions.
- ✅ Designed **Pydantic models** for structured validation of Tutor, Planner, and Quiz outputs, ensuring reliable communication between agents and successful real-time updates in the frontend.

---

## 👩‍💻 Member 3 – <ANUSHKA BISWAL>

### 📅 Study Planner Agent & Backend Services

- 📅 Developed the **Study Planner Agent** using CrewAI to generate personalized day-wise study schedules based on student learning history and academic goals.
- ⚡ Built the core **FastAPI backend**, implementing API endpoints for chat communication, document uploads, and secure frontend-backend interaction using CORS middleware.
- 📂 Implemented document upload functionality using **UploadFile**, FormData, and python-multipart while securely managing API keys using python-dotenv.
- 🌐 Integrated backend APIs with the frontend using JavaScript Fetch API, enabling real-time communication between the user interface and backend services.
- 🛠️ Contributed to backend architecture, API testing, debugging, and deployment preparation while maintaining version control using Git and GitHub.

---

## 👩‍💻 Member 4 – <SANCHITA PANDEY>

### 📝 Quiz Agent Development & System Testing

- 🎯 Developed the **Quiz Agent** using CrewAI, implementing personalized quiz generation based on student profiles, learning history, and router decisions.
- 🧪 Built an automated testing framework using **DeepEval**, evaluating answer relevancy and faithfulness through custom LLM-based evaluation models.
- 📊 Conducted response latency analysis by measuring end-to-end execution time and generating statistical performance metrics.
- 📈 Performed router accuracy benchmarking using balanced engineering datasets to validate intelligent query classification and routing performance.
- 🔧 Assisted in repository restructuring, backend organization, Git workflow management, dependency resolution, and comprehensive system validation.

---

## 👩‍💻 Member 5 – <SANVI SARDANA>

### 🎨 Frontend Development & Academic Tutor Agent

- 💻 Designed and developed the complete **responsive frontend** of EduPilot using HTML5, CSS3, and JavaScript, including Dashboard, Student Profile, Upload Notes, Chat History, Quiz Library, and Study Planner.
- 🎯 Implemented client-side functionality such as form validation, drag-and-drop file uploads, local storage management, dynamic navigation, and interactive user interfaces.
- 🌐 Integrated the frontend with the FastAPI backend for student registration, dashboard operations, profile creation, and seamless API communication.
- 🤖 Developed the **Academic Tutor Agent** using CrewAI and integrated it with the Retrieval-Augmented Generation (RAG) pipeline to provide document-aware academic assistance.
- 🔄 Collaborated using Git and GitHub while validating backend APIs through Swagger UI and ensuring smooth frontend-backend integration across the project.

---# 🙏 Acknowledgements

We sincerely thank our faculty mentors and the open-source community whose tools and frameworks made EduPilot possible.

Special thanks to the developers of CrewAI, FastAPI, LangChain, ChromaDB, LiteLLM, Hugging Face, and Groq for providing the technologies used in this project.
---

⭐ If you found EduPilot interesting, don't forget to star this repository!

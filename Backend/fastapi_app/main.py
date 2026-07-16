#new
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse


from fastapi import FastAPI, File, UploadFile, HTTPException
from patches.groq_patch import apply_patch
apply_patch()
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
from dotenv import load_dotenv
from RAG_agent.Ingestion_pipeline import ingest_uploaded_file

from Memory_agent.memory_service import (
    StudentMemory,
    create_new_student
)

from crew import run_academic_tutor
from chat_history import (
    ChatHistory,
    create_new_session
)

DOCS_FOLDER = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "RAG_agent",
    "docs"
)

#new
PROJECT_ROOT = os.path.dirname(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)

FRONTEND_FOLDER = os.path.join(
    PROJECT_ROOT,
    "frontend")

# .env file ko load karne ke liye
load_dotenv()

app = FastAPI(title="Academic Tutor")

# CORS Settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class StudentRequest(BaseModel):
    student_id: str
    session_id: str
    question: str 

class StudentProfileRequest(BaseModel):
    name: str
    school: str = ""
    stream: str = ""
    college: str = ""
    college_degree: str = ""
    specification: str = ""
    learning_level: str = ""
    class_name: str = ""
    year: str = ""    


@app.post("/api/chat")
def handle_chat(request: StudentRequest):

    try:

        print("="*50)
        print("Student ID:", request.student_id)
        print("Session ID:", request.session_id)
        print("Question:", request.question)
        print("="*50)

        result = run_academic_tutor(
            student_id=request.student_id,
            session_id=request.session_id,
            student_question=request.question
        )

        return {
            "status": "success",
            "response": result
        }

    except Exception as e:
        import traceback
        traceback.print_exc()

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

# =========================================================
# 🚀 UPDATED ENDPOINT: File ko server par permanently save karne ke liye
# =========================================================
@app.post("/api/upload")
async def upload_document(file: UploadFile = File(...)):
    try:
        file_name = file.filename
        content_type = file.content_type
        
        # 1. Folder banayein jahan files save karni hain
        UPLOAD_DIR = "uploaded_docs"
        os.makedirs(UPLOAD_DIR, exist_ok=True) # Agar folder nahi hai toh bana dega
        
        # 2. File ka full permanent destination path set karein
        file_path = os.path.join(UPLOAD_DIR, file_name)
        
        # 3. File content ko read karke local disk par write karein
        contents = await file.read()
        with open(file_path, "wb") as f:
            f.write(contents)

         # Send uploaded file to RAG
        ingest_uploaded_file(file_path)  
            
        file_size_kb = len(contents) / 1024
        
        return {
            "status": "success",
            "message": f"File successfully save ho gayi hai path par: {file_path}",
            "details": {
                "filename": file_name,
                "content_type": content_type,
                "size_kb": round(file_size_kb, 2),
                "saved_at": file_path
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"File save karne me error aaya: {str(e)}")

@app.get("/api/documents")
def get_uploaded_documents():

    try:

        documents = []

        for file in os.listdir(DOCS_FOLDER):

            if os.path.isfile(os.path.join(DOCS_FOLDER, file)):
                documents.append(file)

        return {
            "status": "success",
            "documents": documents
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
    
@app.post("/api/register")
def register_student(profile: StudentProfileRequest):

    try:

        # Create unique student
        student_id = create_new_student()

        # Open that student's JSON
        memory = StudentMemory(f"{student_id}.json")

        # Save profile
        memory.update_profile({

            "name": profile.name,

            "school": profile.school,

            "stream": profile.stream,

            "college": profile.college,

            "college_degree": profile.college_degree,

            "specification": profile.specification,

            "learning_level": profile.learning_level,

            "class": profile.class_name,

            "year": profile.year

        })

        return {

            "status": "success",

            "student_id": student_id,

            "message": "Student registered successfully."

        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )    
    
@app.post("/api/new-chat")
def create_chat(student_id: str):

    try:

        session_id = create_new_session()

        chat = ChatHistory(student_id)

        # Create an empty chat file
        chat.save_message(
            session_id=session_id,
            role="system",
            content="New chat started."
        )

        return {
            "status": "success",
            "session_id": session_id
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
@app.get("/api/chat-sessions/{student_id}")
def get_chat_sessions(student_id: str):

    try:

        chat = ChatHistory(student_id)

        sessions = chat.list_sessions()

        return {
            "status": "success",
            "sessions": sessions
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
@app.get("/api/chat/{student_id}/{session_id}")
def load_chat(student_id: str, session_id: str):

    try:

        chat = ChatHistory(student_id)

        conversation = chat.load_chat(session_id)

        if conversation is None:

            raise HTTPException(
                status_code=404,
                detail="Session not found."
            )

        return {
            "status": "success",
            "conversation": conversation["messages"]
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
# =========================================================
# GET ALL SAVED QUIZZES
# =========================================================

@app.get("/api/quizzes/{student_id}")
def get_saved_quizzes(student_id: str):

    try:

        memory = StudentMemory(f"{student_id}.json")

        quizzes = memory.get_saved_quizzes()

        return {
            "status": "success",
            "quizzes": quizzes
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

# =========================================================
# GET ALL SAVED STUDY PLANS
# =========================================================

@app.get("/api/plans/{student_id}")
def get_saved_plans(student_id: str):

    try:

        memory = StudentMemory(f"{student_id}.json")

        plans = memory.get_saved_plans()

        return {
            "status": "success",
            "plans": plans
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

app.mount(
    "/static",
    StaticFiles(directory=FRONTEND_FOLDER),
    name="static"
)


@app.get("/")
def serve_home():
    return FileResponse(
        os.path.join(FRONTEND_FOLDER, "agent.html")
    )


@app.get("/form")
def serve_form():
    return FileResponse(
        os.path.join(FRONTEND_FOLDER, "form.html")
    )


@app.get("/dashboard")
def serve_dashboard():
    return FileResponse(
        os.path.join(FRONTEND_FOLDER, "dashboard.html")
    )

@app.get("/chathistory")
def serve_chathistory():
    return FileResponse(
        os.path.join(FRONTEND_FOLDER, "chathistory.html")
    )

@app.get("/notes")
def serve_notes():
    return FileResponse(
        os.path.join(FRONTEND_FOLDER, "notes.html")
    )

@app.get("/quiz")
def serve_quiz():
    return FileResponse(
        os.path.join(FRONTEND_FOLDER, "quiz.html")
    )

@app.get("/studyplanner")
def serve_studyplanner():
    return FileResponse(
        os.path.join(FRONTEND_FOLDER, "studyplanner.html")
    )
from Memory_agent.memory_service import create_new_student, StudentMemory
from chat_history import create_new_session
from patches.groq_patch import apply_patch
apply_patch()
from crew import run_academic_tutor

# -------------------------
# Create Student
# -------------------------

student_id = create_new_student()

print(f"\nStudent ID: {student_id}")

memory = StudentMemory(f"{student_id}.json")

memory.update_profile({
    "name": "Ishita",
    "college": "ABC College",
    "college_degree": "B.Tech",
    "specification": "CSE",
    "learning_level": "Intermediate",
    "year": "2"
})

print("Student profile created successfully!")

# -------------------------
# First Chat Session
# -------------------------

session_id = create_new_session()

print(f"Session ID: {session_id}")

print("\nType your questions below.")
print("Type 'new' to start a new chat.")
print("Type 'exit' to quit.\n")

while True:

    question = input("You: ")

    if question.lower() == "exit":
        print("\nGoodbye!")
        break

    if question.lower() == "new":

        session_id = create_new_session()

        print("\n----------------------------")
        print("Started New Chat")
        print("Session ID:", session_id)
        print("----------------------------\n")

        continue

    response = run_academic_tutor(
        student_id=student_id,
        session_id=session_id,
        student_question=question
    )

    print("\nEduPilot AI:")
    print(response)
    print()
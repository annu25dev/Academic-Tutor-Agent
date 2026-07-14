from patches.groq_patch import apply_patch
apply_patch()
from crew import run_academic_tutor

while True:
    question = input("Enter your question: ")

    if question.lower() == "exit":
        break

    result = run_academic_tutor(question)

    print("\n================ OUTPUT ================\n")

    print(result)
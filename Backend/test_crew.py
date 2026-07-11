from patches.groq_patch import apply_patch
apply_patch()
from crew import run_academic_tutor

question = input("Enter your question: ")

result = run_academic_tutor(question)

print("\n================ OUTPUT ================\n")

print(result)
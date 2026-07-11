from crewai import Task
from .agent import quiz_agent


def quiz_task(student_question: str, student_profile: str = "None", previous_learning: str = "None"):
    
     # output format instruction
    format_instruction = "Return a raw JSON object with keys: quiz_title, difficulty, and questions array containing question_text, options, correct_answer, and explanation. Do not wrap in markdown blocks."

    return Task(
        description=f"""
        Analyze the student request: '{student_question}' and build a personalized 5-question quiz.
        
        Personalization Parameters:
        - Student Profile Context: {student_profile}
        - Previous Learning History: {previous_learning}
        
        Requirements:
        - Strictly restrict question types to: Multiple Choice (MCQs), Fill-in-the-blanks, or One-word answers. Do NOT generate long-form subjective questions.
        - Base the quiz questions entirely on the provided student profile and previous learning history to keep it highly personalized.
        - ALWAYS use the Academic RAG Tool first before generating a quiz.
        - Read the retrieved context carefully.
        - If relevant context is available, generate quiz questions ONLY from the retrieved notes.
        - If no relevant context is retrieved, generate quiz questions using your own knowledge.
        - Mention the document source whenever available.
        """,
        expected_output=format_instruction,
        agent=quiz_agent
    )
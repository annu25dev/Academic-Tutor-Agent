from crewai import Task
from .agent import quiz_agent
from Pydantic_models import QuizOutput


def quiz_task(student_question: str, student_profile: str = "None", previous_learning: str = "None",previous_conversation: str ="None"):
    

    return Task(
        description=f"""
        Analyze the student request: '{student_question}' and build a personalized 5-question quiz.
        
        Personalization Parameters:
        - Student Profile Context: {student_profile}
        - Previous Learning History: {previous_learning}
        -previous conversation:{previous_conversation}

        
        Requirements:
        - Strictly restrict question types to: Multiple Choice (MCQs), Fill-in-the-blanks, or One-word answers. Do NOT generate long-form subjective questions.
        - Base the quiz questions entirely on the provided student profile and previous learning history to keep it highly personalized.
        - ALWAYS use the Academic RAG Tool first before generating a quiz.
        - Read the retrieved context carefully.
        - If relevant context is available, generate quiz questions ONLY from the retrieved notes.
        - If no relevant context is retrieved, generate quiz questions using your own knowledge.
        - Read the retrieved syllabus or study material carefully.
        - If relevant context is retrieved, generate the QUIZ using ONLY the document(s) that are directly relevant to the student's current request.
        - Ignore any retrieved document that is unrelated or only partially related to the student's question, even if it is returned by the RAG tool. Do not mix information from multiple documents unless they discuss the same topic.
        - If multiple documents are retrieved, first determine which document best matches the student's query, and base the study plan only on that document.
        - Mention the document source that is apt to the prompt given by user whenever available.
        """,
        expected_output=
        """
        Create a personalized 5-question quiz.

        The quiz should:
        - Have a title.
        - Have a difficulty level.
        - Contain 5 questions.
        - Each question should have options, a correct answer and an explanation.
        """,
        agent=quiz_agent,
        output_pydantic=QuizOutput
    )
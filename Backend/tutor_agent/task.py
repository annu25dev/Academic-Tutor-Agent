from crewai import Task
from .agent import tutor_agent
from llm import llm
from Pydantic_models import TutorOutput

def Tutor_task(student_question, student_profile, previous_learning):

    task = Task(

        description=f"""
You are teaching a student.
Question:
{student_question}
Student Profile:
{student_profile}
Previous Learning History:
{previous_learning}
Instructions:
1. Greet the student by name whenever possible.
2. Personalize the explanation according to the student's profile
   (class, preferred subject, learning level, and exam date).
3. If the exam is near, focus more on important concepts,
   revision tips, and high-weightage topics.
4. If previous learning history is available,
   continue from where the student stopped instead of
   explaining everything from the beginning.
5. Explain the topic in very simple language.
6. Break difficult concepts into small, easy-to-understand steps.
7. Give at least one real-life analogy.
8. If the topic belongs to programming,
   include a code example with explanation.
9. Mention common mistakes students usually make.
10. Generate one practice question.
11. End with a short summary.
12. Suggest what the student should study next.
13. ALWAYS call the Academic RAG Tool first before answering.
14. Read the retrieved context carefully.
15. If the retrieved context contains relevant information,
answer ONLY from that context.
16. If the retrieved context is empty,
then answer using your own knowledge.
17. Mention the document source whenever available.
""",

        expected_output="""
Generate the following information:

- topic: The main academic topic discussed in the student's question.
- response: A complete, personalized learning response.

The response should include the following elements:
A highly personalized learning response that includes:
• Greeting using the student's name.
• Personalized explanation according to learning level.
• Continuation from previous learning whenever available.
• Easy step-by-step explanation.
• Real-life analogy.
• Code example (if applicable).
• Diagram or flowchart description (if applicable).
• Common mistakes.
• One practice question.
• Short summary.
• Suggested next topic for learning.
""",

        agent=tutor_agent,
        output_pydantic=TutorOutput

    )

    return task
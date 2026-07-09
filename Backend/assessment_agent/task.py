from crewai import Task
from .agent import assessment_agent


def assessment_task(

    student_question,

    student_answer,

    student_profile,

    previous_learning

):

    task = Task(

        description=f"""

You are the Assessment Agent of a Personalized Academic Tutor.

Student Question:

{student_question}

student Answer:

{student_answer}

Student Profile:

{student_profile}

Previous Learning:

{previous_learning}

Your responsibilities:

1. Understand the student's request.

2. If student Answer is empty or not provided:
generate descriptive, case-study, application-based,
scenario-based, or coding questions.

3. Never generate MCQs, True/False,
Fill in the blanks, or objective quizzes.
These belong exclusively to the Quiz Agent.

4. If the student Answer is provided:
evaluate it like a real teacher.

5. Score the answer on:

• Conceptual Accuracy (0-10)

• Depth of Understanding (0-10)

• Clarity of Explanation (0-10)

• Application Ability (0-10)

6. Identify:

• Correct concepts

• Missing concepts

• Misconceptions

• Logical mistakes

7. Generate:

• Overall Score

• Strengths

• Weaknesses

• SWOT Analysis

• Personalized Recommendations

8. If the student requests answer improvement,
rewrite the answer,
explain the improvements,
and suggest how to score better.

Always personalize the assessment using
Student Profile and Previous Learning.

Never teach the complete topic again.

""",

        expected_output="""

Return a personalized assessment according to the student's request.

Possible outputs include:

• Descriptive assessment questions

• Coding questions

• Case-study questions

• Answer evaluation

• Parameter-wise scores

• SWOT Analysis

• Personalized Recommendations

• Improved Answer (if requested)

""",

        agent=assessment_agent

    )

    return task
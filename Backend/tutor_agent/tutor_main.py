from tutor_crew import create_academic_tutor_crew


crew = create_academic_tutor_crew()

result = crew.kickoff(

    inputs={

        "name": "Emma",

        "student_question":
        "Explain recursion in Python.",

        "academic_level":
        "Beginner",

        "student_class":
        "First Year B.Tech",

        "learning_style":
        "Visual Learner",

        "strengths":
        "Logical Thinking",

        "weaknesses":
        "Recursion",

        "exam_date":
        "2026-08-10",

        "current_topic":
        "Functions",

        "previous_learning":
        "Student understands loops and conditional statements."

    }

)

print(result)
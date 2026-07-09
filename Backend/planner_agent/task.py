from crewai import Task
from .agent import studyplanner_agent


def studyplanner_task(student_question, student_profile, previous_learning):
    
    return Task(
        description=f"""
        You are helping a student create a personalized study plan.

        The student's question/request:
        {student_question}

        Their current learning profile:
        {student_profile}

        Topics they have already studied:
        {previous_learning}

        Your job is to:
        
        1. Understand the student's goal and identify the important topics they need to learn.
        2. Arrange these topics in a logical learning order, starting from fundamentals and moving toward advanced concepts.
        3. Create a realistic timeline (daily or weekly plan) based on the student's available time, current level, and learning speed.
        4. Add practical tasks, exercises, projects, or revision activities at important milestones.
        5. Make sure the plan is achievable and motivating for the student.
        """,

        expected_output="""
        Provide a clear and personalized study roadmap in markdown format.

        The roadmap should include:
        - Learning goals
        - Topic sequence
        - Day-wise or week-wise schedule
        - Time estimates
        - Practice exercises or checkpoints
        - Revision strategy

        The plan should feel practical and easy for a student to follow.
        """,

        agent=studyplanner_agent
    )
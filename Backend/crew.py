from crewai import Crew, Process
# Memory
from Memory_agent.memory_service import StudentMemory
# Router
from router_agent.agent import router_agent
from router_agent.task import router_task
# Assessment
from assessment_agent.agent import assessment_agent
from assessment_agent.task import assessment_task
# Tutor
from tutor_agent.agent import tutor_agent
from tutor_agent.task import Tutor_task
# Planner
from planner_agent.agent import planner_agent
from planner_agent.task import planner_task
# Quiz
from quiz_agent.agent import quiz_agent
from quiz_agent.task import quiz_task


def run_academic_tutor(student_question: str):

    # Load Student Memory

    memory = StudentMemory()

    student_profile = memory.get_profile()

    previous_learning = memory.get_learning_history()

    # Router Task

    task = router_task(
        student_question,
        student_profile,
        previous_learning
    )

    # Router Crew


    router_crew = Crew(
        agents=[router_agent],
        tasks=[task],
        process=Process.sequential,
        verbose=True
    )

    # Execute Router

    router_result = router_crew.kickoff()

    router_decisions = [
        decision.strip()
        for decision in str(router_result).split("→")
    ]

    print("Router Decisions:")

    for decision in router_decisions:
        print("-", decision)

    # Store outputs of all executed agents

    results = []

    # Execute Every Agent Returned

    for decision in router_decisions:

        # Assessment

        if decision == "Assessment":

            assessment = assessment_task(
                student_question=student_question,
                student_answer="",
                student_profile=student_profile,
                previous_learning=previous_learning
            )

            assessment_crew = Crew(
                agents=[assessment_agent],
                tasks=[assessment],
                process=Process.sequential,
                verbose=True
            )

            results.append(str(assessment_crew.kickoff()))

        # Tutor

        elif decision == "Tutor":

            tutor = Tutor_task(
                student_question=student_question,
                student_profile=student_profile,
                previous_learning=previous_learning
            )

            tutor_crew = Crew(
                agents=[tutor_agent],
                tasks=[tutor],
                process=Process.sequential,
                verbose=True
            )

            results.append(str(tutor_crew.kickoff()))

        # Planner

        elif decision == "Planner":

            planner = planner_task(
                student_question=student_question,
                student_profile=student_profile,
                previous_learning=previous_learning
            )

            planner_crew = Crew(
                agents=[planner_agent],
                tasks=[planner],
                process=Process.sequential,
                verbose=True
            )

            results.append(str(planner_crew.kickoff()))

        # Quiz

        elif decision == "Quiz":

            quiz = quiz_task(
                student_question=student_question,
                student_profile=student_profile,
                previous_learning=previous_learning
            )

            quiz_crew = Crew(
                agents=[quiz_agent],
                tasks=[quiz],
                process=Process.sequential,
                verbose=True
            )

            results.append(str(quiz_crew.kickoff()))

        # Unknown Agent 

        else:

            results.append(f"Unknown router decision: {decision}")

    # Return Final Combined Output

    return "\n\n".join(results)
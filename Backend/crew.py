from crewai import Crew, Process
import pydantic
from chat_history import ChatHistory
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

#Every request will tell who is asking, which session and what is the question
def run_academic_tutor(student_id: str, session_id: str, student_question: str):

    # Load Student Memory

    memory = StudentMemory(f"{student_id}.json")
    #Student conversations will be stored at the right place 
    chat = ChatHistory(student_id)

    print("Chat folder:", chat.chat_folder)

    chat.save_message(
    session_id=session_id,
    role="user",
    content=student_question
)

    print("User message saved successfully.")

    student_profile = memory.get_profile()

    previous_learning = memory.get_learning_history()
    
    #Every user question will be stored in the chat history of that particular session
   
    print("Assistant message saved successfully.")
    # Router Task

    task = router_task(
        student_question,
        student_profile,
        previous_learning
    )
    # --------------------------
    # Router Crew
    # --------------------------


    router_crew = Crew(
        agents=[router_agent],
        tasks=[task],
        process=Process.sequential,
        verbose=True
    )

    print("Starting Router...")

    router_result = router_crew.kickoff()

    print("\nRaw Router Output:")

    print(router_result)

    # --------------------------
    #Parse Router Output
    # --------------------------

    router_tasks={}

    for line in str(router_result).split("\n"):

        line = line.strip()

        if not line:
            continue

        if ":" not in line:
            continue

        agent_name, task_text = line.split(":",1)

        router_tasks[agent_name.strip()] = task_text.strip()

    print("\nParsed Router Tasks:")

    for agent_name, task_text in router_tasks.items():
        print(f"- {agent_name} - > {task_text}")

    
    #--------------------------
    # Execute Agents
    #--------------------------
    
    # Store outputs of all executed agents

    results = []
    
    for decision, agent_task in router_tasks.items():
        decision = decision.strip().lower()

        #---------------- Assessment ---------------

        if "assessment" in decision:

            assessment = assessment_task(
                student_question=agent_task,
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

        #-------------- Tutor ---------------

        elif "tutor" in decision:

            tutor = Tutor_task(
                student_question=agent_task,
                student_profile=student_profile,
                previous_learning=previous_learning
            )

            tutor_crew = Crew(
                agents=[tutor_agent],
                tasks=[tutor],
                process=Process.sequential,
                verbose=True
            )

            tutor_result = tutor_crew.kickoff()

            topic = tutor_result.pydantic.topic

            response = tutor_result.pydantic.response
            memory.update_learning_history(topic=topic)
            results.append(response)
            

        #--------------- Planner -----------------

        elif "planner" in decision:

            planner = planner_task(
                student_question=agent_task,
                student_profile=student_profile,
                previous_learning=previous_learning
            )

            planner_crew = Crew(
                agents=[planner_agent],
                tasks=[planner],
                process=Process.sequential,
                verbose=True
            )

            planner_result=planner_crew.kickoff()
            
            topic = planner_result.pydantic.topic

            response = planner_result.pydantic.response
            
            #For storing to memory agent
            memory.save_plan(topic=topic,
                              plan=response)

            #OUTPUT
            results.append(response)

        #----------------------Quiz---------------------

        elif "quiz" in decision:

            quiz = quiz_task(
                student_question=agent_task,
                student_profile=student_profile,
                previous_learning=previous_learning
            )

            quiz_crew = Crew(
                agents=[quiz_agent],
                tasks=[quiz],
                process=Process.sequential,
                verbose=True
            )

            quiz_result=quiz_crew.kickoff()

            topic = quiz_result.pydantic.topic

            response = quiz_result.pydantic.response

            memory.save_quiz(
                topic=topic,
                quiz=response
            )

            results.append(response)


        # ------------------- Unknown Agent -------------------

        else:

            results.append(f"Unknown router decision: {decision}")
    
    # ----------------------------
    # Return Final Combined Output
    # ----------------------------

   
    final_response = "\n\n".join(results)

    #Assistant response will be stored in the chat history of that particular session
    chat.save_message(
            session_id=session_id,
            role="assistant",
            content=final_response
        )

    return final_response
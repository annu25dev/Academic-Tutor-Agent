from crewai import Task
from Backend.Memory_agent.agent import memory_agent

memory_task = Task(
   description="""
    Manage the student's long-term memory.

    Depending on the request, you may:
    - Store or update the student's personal profile.
    - Retrieve the student's personal profile.
    - Store or update the student's learning history.
    - Retrieve the student's learning history.
    - Store or retrieve student progress.
    - Save quiz results.
    - Save feedback.
    - Retrieve any previously stored information when requested.

    Ensure all information is stored accurately and consistently.
    """,

    expected_output="""
    Return a confirmation that the memory has been updated,
    or return the requested memory information in a structured format.
    """,

    agent=memory_agent
)
from crewai import Crew

from tutor_agent import academic_tutor
from tutor_task import academic_tutoring_task


def create_academic_tutor_crew():

    return Crew(

        agents=[
            academic_tutor
        ],

        tasks=[
            academic_tutoring_task
        ],

        verbose=True
    )
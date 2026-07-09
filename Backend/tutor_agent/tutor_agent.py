from crewai import Agent
from llm import llm

from tutor_config import (
    TUTOR_GOAL,
    TUTOR_BACKSTORY
)

academic_tutor = Agent(
    role="Academic Tutor",

    goal=TUTOR_GOAL,

    backstory=TUTOR_BACKSTORY,

    llm=llm,

    verbose=True,

    allow_delegation=False
)
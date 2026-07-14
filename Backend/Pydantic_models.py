from pydantic import BaseModel

class TutorOutput(BaseModel):
    topic: str
    response: str


class PlannerOutput(BaseModel):
    topic: str
    response: str

class QuizOutput(BaseModel):
    topic: str
    response: str
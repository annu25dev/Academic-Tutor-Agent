from crewai import Agent
from llm import llm  
from RAG_agent.rag_tool import rag_tool

quiz_agent = Agent(
    role="Quiz Agent",
    
    goal="""
    Design highly dynamic, context_aware assessment materials_focusing
    strictly on conceptual MCQs, fill-in-the-blank queries, and one-word
    type questions tailored precisely to the student's level and background.
    """,
    
    backstory="""
    You are an academic evaluator responsible for creating quick-recall
    quizzes (MCQs, blanks, and short answers) that verify basic comprehension
    and core retention without requiring deep, long_form essay grading.
    """,
    tools=[rag_tool],
    
    llm=llm,
    verbose=True,
    allow_delegation=False  
)
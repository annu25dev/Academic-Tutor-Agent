#Creating a custom RAG tool
from crewai.tools import tool
from Backend.RAG_agent.Retrieval_pipeline import answer_question

@tool("Academic RAG Tool")

def rag_tool(question:str):
    '''
    1. Search the uploaded academic documents and answer the student's question.
    2. Use this tool whenever the answer may exist in the uploaded study material.'''

    result = answer_question(question)

    answer=result["answer"]
    sources="\n".join(result["sources"])

    return f""" Answer:{answer} 
          Sources: {sources}"""
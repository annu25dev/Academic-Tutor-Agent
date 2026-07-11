#Creating a custom RAG tool
from crewai.tools import tool
from RAG_agent.Retrieval_pipeline import retrieve_context

@tool("Academic RAG Tool")

def rag_tool(question:str):
     
     """
    Retrieves relevant context from uploaded academic documents.

    Use this tool whenever the student asks something that may be
    answered using uploaded PDFs, PPTs, DOCX, TXT, CSV or Excel files.

    This tool DOES NOT generate the final answer.
    It only returns the retrieved context and document sources.
    """
    #'''
    #1. Search the uploaded academic documents and answer the student's question.
    #2. Use this tool whenever the answer may exist in the uploaded study material.'''

     result = retrieve_context(question)
     return {
        "context": result["context"],
        "sources": result["sources"]
         }

     #answer=result["answer"]
     #sources="\n".join(result["sources"])

     #return f""" Answer:{answer} 
          #Sources: {sources}"""
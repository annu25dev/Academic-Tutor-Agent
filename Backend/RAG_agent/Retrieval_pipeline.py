#from llm import llm
import os
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
#from langchain_groq import ChatGroq
#from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
load_dotenv()
#groq=os.getenv("GROQ_API_KEY")
#llm=ChatGroq(model="llama-3.3-70b-versatile", temperature=0.2,api_key=groq)
persistent_directory = "RAG_agent/db/chroma_db"

#----------------------------------1. LOAD EMBEDDINGS & VECTOR STORE---------------------------------

embedding_model=HuggingFaceEmbeddings(model_name="BAAI/bge-small-en-v1.5")

db=Chroma(
        persist_directory=persistent_directory,
        embedding_function=embedding_model,
        collection_metadata={"hnsw:space":"cosine"}
)

#To check if it's not empty
print(db._collection.count())

#----------------------------------2. SEARCH FOR RELEVANT DOCUMENTS---------------------------------

#query=input("Enter your query: ")

def retrieve_context(query:str):
    retriever=db.as_retriever(search_kwargs={"k":5})

    relevant_docs=retriever.invoke(query)

    #If multiple chunks come from the same file, the file name is displayed only once
    sources=set()

    #To mention the source
    for doc in relevant_docs:
        sources.add(os.path.basename(doc.metadata["source"]))
    context="\n\n".join([doc.page_content for doc in relevant_docs])

#-------------------------------------3. COMBINING WITH LLM------------------------------------------

   # prompt=ChatPromptTemplate.from_template("""
       # You are an intelligent academic tutor.

       #1. Answer the user's question ONLY using the context provided below.

    #2. If the answer is not present in the context, say:
    #"I don't have enough information in the provided documents."

   # 3. Context:
    #{context}

   # 4. Question:
    #{question}

    #Answer:
    #""")

    #formatted_prompt=prompt.format(context=context, question=query)

    #response=llm.invoke(formatted_prompt)
#print(f"\nUser Query:  {query}")
   # return{"answer":response.content,"sources":list(sources)}
    return {
       "context":context,
       "sources":list(sources)
   }
#Displaying Results
   
#print("\n-------ANSWER-------")
#print(response.content)
#print("\nSources: ")
#for i,source in enumerate(sources,start=1):
#        print(f"{i}. {source}")



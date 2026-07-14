#from llm import llm
import os
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
#from langchain_groq import ChatGroq
#from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
load_dotenv()
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


def retrieve_context(query:str):
    retriever=db.as_retriever(search_kwargs={"k":2})

    relevant_docs=retriever.invoke(query)

    #If multiple chunks come from the same file, the file name is displayed only once
    sources=set()

    #To mention the source
    for doc in relevant_docs:
        sources.add(os.path.basename(doc.metadata["source"]))
    context="\n\n".join([doc.page_content for doc in relevant_docs])

    return {
       "context":context,
       "sources":list(sources)
   }




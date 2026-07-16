import shutil
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DOCS_PATH = os.path.join(BASE_DIR, "docs")
DB_PATH = os.path.join(BASE_DIR, "db", "chroma_db")
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import (
    TextLoader,
    DirectoryLoader,
    PyPDFLoader,
    CSVLoader,
    UnstructuredExcelLoader,
    UnstructuredPowerPointLoader,
    UnstructuredWordDocumentLoader
)
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from dotenv import load_dotenv
load_dotenv()

#--------------------------------------1. UPLOADING FILE-----------------------------------------

def upload_document(file_path,docs_path):
    destination=os.path.join(docs_path,
                             os.path.basename(file_path))
    shutil.copy(file_path, destination)
    print("\n File Uploaded Successfully!!!")

#--------------------------------------2. DATA LOADING------------------------------------------

def load_documents(docs_path):
    #Loads all text files from docs directory
    print(f"\nLoading documents from {docs_path}...")

    #Checking if docs directory exists
    if not os.path.exists(docs_path):
        raise FileNotFoundError(f"\nThe directory {docs_path} does not exist. Please create it "
                                 "and add your files.")
    
    #All file types
    loaders = {
    "*.txt": TextLoader,
    "*.pdf": PyPDFLoader,
    "*.docx": UnstructuredWordDocumentLoader,
    "*.pptx": UnstructuredPowerPointLoader,
    "*.csv": CSVLoader,
    "*.xlsx": UnstructuredExcelLoader,
    }

    documents = []

    #load all types of files from the docs directory
    for pattern, loader_cls in loaders.items():
       loader = DirectoryLoader(
         path=docs_path,
         glob=pattern,
         loader_cls=loader_cls
    )
       docs=loader.load()

       #Adding source and metadata

       for doc in docs:
           doc.metadata["source"]=os.path.basename(doc.metadata["source"])
       documents.extend(docs)

    if len(documents)==0:
        raise FileNotFoundError(f"\nThe directory {docs_path} does not exist. Please create it "
                                 "and add your files.")
    
    else:
        print("\nFile Loaded Successfully!!!")

    return documents

#--------------------------------------2. CHUNKING------------------------------------------

def split_documents(documents,chunk_size=800,chunk_overlap=0):

    #Split documents into smaller chunks
    print("\nSplitting documents into chunks...")
    text_splitter=CharacterTextSplitter(chunk_size=chunk_size,chunk_overlap=chunk_overlap)
    chunks=text_splitter.split_documents(documents)
    
    if len(chunks)>0:
        print("\nChunking done successfully!!!")
        print(f"\n... and {len(chunks)} chunks are made.")

    return chunks

#---------------------   -----3. EMBEDDING & STORING IN VECTOR DATABASE----------------------------

def create_vector_store(chunks, persist_directory=DB_PATH):
    #Creating and persisting ChromaDB Vector Store
    print("\n Creating embeddings amd storing in ChromaDB")

    embedding_model=HuggingFaceEmbeddings(model_name="BAAI/bge-small-en-v1.5")

    #Creating ChromaDB vector store
    print("\n Creating vector store")
    vector_store=Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory=persist_directory,
        collection_metadata={"hnsw:space":"cosine"}
    )

    #To check if it's not empty
    print(vector_store._collection.count())

    print("\n Finished creating Vector Store")
    print(f"\n Vector store created and saved to {persist_directory}")
    return vector_store

#--------------------------------------4. CALLING FUNCTIONS---------------------------------
def ingest_uploaded_file(file_path):
    """
    Takes the uploaded file path from FastAPI,
    copies it into RAG_agent/docs,
    loads all documents,
    splits them into chunks,
    and stores them in ChromaDB.
    """

    # Step 1: Copy uploaded file into docs folder
    upload_document(file_path, docs_path=DOCS_PATH)

    # Step 2: Load all documents from docs folder
    documents = load_documents(docs_path=DOCS_PATH)

    # Step 3: Split into chunks
    chunks = split_documents(documents)

    # Step 4: Store embeddings in ChromaDB
    create_vector_store(chunks)
def main():
    print("Main Function")
 
    file_path=input("Enter file path: ").strip().strip('"')

    #1. Uploading The File
    upload_document(file_path, docs_path="DOCS_PATH")

    #2. Loading The Files
    documents=load_documents(docs_path="DOCS_PATH")

    #3. Chunking the files
    chunks=split_documents(documents)

    #4. Embedding and storing in Vector DB
    vector_store=create_vector_store(chunks)

if __name__=="__main__":
    main()
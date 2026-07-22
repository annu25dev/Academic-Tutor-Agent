import os
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

load_dotenv()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "db", "chroma_db")

# ----------------------------------
# Embedding Model
# ----------------------------------

embedding_model = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-en-v1.5"
)

# ----------------------------------
# Retrieve Context
# ----------------------------------

def retrieve_context(query: str):

    db = Chroma(
        persist_directory=DB_PATH,
        embedding_function=embedding_model,
        collection_metadata={"hnsw:space": "cosine"}
    )

    print("Total Chunks:", db._collection.count())

    docs_and_scores = db.similarity_search_with_score(
        query,
        k=3
    )

    if not docs_and_scores:
        return {
            "context": "",
            "sources": []
        }

    print("\nRetrieved Chunks:\n")

    for doc, score in docs_and_scores:
        print(
            f"{os.path.basename(doc.metadata.get('source','Unknown'))} | Score: {score}"
        )

    # ----------------------------------------------------
    # Find the best matching document
    # ----------------------------------------------------

    best_doc = docs_and_scores[0][0]

    best_filename = os.path.basename(
        best_doc.metadata.get("source", "Unknown")
    )

    print("\nSelected Document:", best_filename)

    # ----------------------------------------------------
    # Keep only chunks from best document
    # ----------------------------------------------------

    relevant_docs = []

    for doc, score in docs_and_scores:

        filename = os.path.basename(
            doc.metadata.get("source", "Unknown")
        )

        if (
            filename == best_filename
            and score < 0.50
        ):
            relevant_docs.append(doc)

    # ----------------------------------------------------
    # Fallback
    # ----------------------------------------------------

    if len(relevant_docs) == 0:

        for doc, score in docs_and_scores:

            filename = os.path.basename(
                doc.metadata.get("source", "Unknown")
            )

            if filename == best_filename:
                relevant_docs.append(doc)

            if len(relevant_docs) == 2:
                break

    context = "\n\n".join(
        [doc.page_content for doc in relevant_docs]
    )

    return {
        "context": context,
        "sources": [best_filename]
    }
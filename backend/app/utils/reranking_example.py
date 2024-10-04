from typing import List
from langchain.docstore.document import Document
from langchain_openai import OpenAIEmbeddings

from app.executors.vector_store import create_neo4j_vector_store
from app.executors.retriever import CustomRetriever


chunks = [
    "The capital of France is great.",
    "The capital of France is huge.",
    "The capital of France is beautiful.",
    """Have you ever visited Paris? It is a beautiful city where you can eat delicious food and see the Eiffel Tower. 
    I really enjoyed all the cities in france, but its capital with the Eiffel Tower is my favorite city.""", 
    "I really enjoyed my trip to Paris, France. The city is beautiful and the food is delicious. I would love to visit again. Such a great capital city."
]
docs = [Document(page_content=sentence) for sentence in chunks]


def compare_rag_techniques(query: str, docs: List[Document] = docs) -> None:
    embeddings = OpenAIEmbeddings()
    graph = create_neo4j_vector_store()
    vectorstore = graph.from_documents(docs, embeddings)

    print("Comparison of Retrieval Techniques")
    print("==================================")
    print(f"Query: {query}\n")
    
    print("Baseline Retrieval Result:")
    baseline_docs = vectorstore.similarity_search(query, k=2)
    for i, doc in enumerate(baseline_docs):
        print(f"\nDocument {i+1}:")
        print(doc.page_content)

    print("\nAdvanced Retrieval Result:")
    custom_retriever = CustomRetriever(vectorstore=vectorstore)
    advanced_docs = custom_retriever.get_relevant_documents(query)
    for i, doc in enumerate(advanced_docs):
        print(f"\nDocument {i+1}:")
        print(doc.page_content)


query = "what is the capital of france?"
compare_rag_techniques(query, docs)

from typing import List
from langchain_community.vectorstores.neo4j_vector import Neo4jVector
from langchain.docstore.document import Document

from app.utils.loaders import split_docs
from app.workers.ingester.file_loader import split_into_graph
from app.workers.ingester.neo4jgraphingestor import Neo4jGraphInjestor
from config.config import Config



def create_neo4j_vector_store(id: int, docs: str) -> Neo4jVector:
    docs = Document(
            page_content=docs,
            metadata={"source": "local"}
        )
    print("Splitting docs..............")
    docs = split_docs([docs])
    print("Splitting into graph..............")
    graph_docs = split_into_graph(docs)
    print("Ingesting into graph..............")
    graph_ingester = Neo4jGraphInjestor(graph_docs, str(id), Config)
    graph = graph_ingester.ingest_documents(str(id))

    graph = graph_ingester.ingest_documents(str(id))
    print("Ingested Docs..............")

    return graph

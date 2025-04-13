from typing import List
from app.workers.ingester.neo4j_graph import Neo4jGraph
from langchain_community.graphs.graph_document import GraphDocument
from app.config.config import Config


class Neo4jGraphInjestor:
    def __init__(self, docs: List[GraphDocument], id:str, config: Config=Config()):
        self.config = config
        self.docs = docs
        self.graph = Neo4jGraph(
            url=self.config.NEO4J_URI,
            username=self.config.NEO4J_USER,
            password=self.config.NEO4J_PASSWORD,
            sanitize=True,
            BASE_ENTITY_LABEL=f"__Entity__{id}",
        )
        # self.embeddings = OpenAIEmbeddings(openai_api_key=self.config.OPENAI_API_KEY)

    def ingest_documents(self, id:str) -> Neo4jGraph:
        print("Adding documents to graph")
        try:
            self.graph.add_graph_documents(self.docs, True, True)
        except Exception as e:
            print(f"Error adding documents to graph: {e}")
            raise e
        print("Adding documents to graph complete")
        print("Creating full-text index")
        try:
            fulltext_index = self.create_fulltext_index(id)
        except Exception as e:
            print(f"Error creating full-text index: {e}")
            raise e
        print("Full-text index created")
        return self.graph
    

    def create_fulltext_index(self, id:str):
        """
        Create a full-text index for the entities in the database.

        This function creates a full-text index for the entities in the database
        based on the source provided. It uses the source to filter the entities
        to be indexed.
        """
        index_name = f'entity_{id}'
        entity_name = f'__Entity__{id}'
        results = self.graph.query(
            f"CREATE FULLTEXT INDEX {index_name} IF NOT EXISTS FOR (e:{entity_name}) ON EACH [e.id]",
            )
        return results
    


from app.utils.loaders import *
from langchain_community.vectorstores.neo4j_vector import Neo4jVector
import neo4j

from config.config import Config



def create_neo4j_vector_store() -> Neo4jVector:
    neo4j_uri = Config.NEO4J_URI
    neo4j_user = Config.NEO4J_USER
    neo4j_password = Config.NEO4J_PASSWORD
    neo4j_driver = neo4j.GraphDatabase.driver(neo4j_uri, auth=(neo4j_user, neo4j_password))

    return neo4j_driver

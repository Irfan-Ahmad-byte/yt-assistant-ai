from langchain_community.graphs import Neo4jGraph
from config.config import Config



graph = Neo4jGraph(
    url=Config.NEO4J_URI,
    username=Config.NEO4J_USER,
    password=Config.NEO4J_PASSWORD,
    sanitize=True,
    )
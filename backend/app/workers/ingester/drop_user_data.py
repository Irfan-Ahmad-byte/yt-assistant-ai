from utils.llm import prepare_graph


graph = prepare_graph.graph

def drop_data(id:str):
    # match (e) -- (n) where n.source contains('1231') detach delete e, n
    # MATCH (n:`__Entity__`{source:source}) detach delete n
    index = f'entity_{id}'
    entity = f"__Entity__{id}"
    try:
        graph.query(
            "MATCH (e) -- (n) WHERE n.source CONTAINS($ID) DETACH DELETE e, n"
            , {"ID": id}
        )
        # graph.query(
        #     "MATCH (n:$ENTITY) DETACH DELETE n"
        #     , {"ENTITY": entity}
        # )
        # graph.query(
        #     "DROP INDEX $INDEX IF EXISTS"
        #     , {"INDEX": index}
        # )
    except Exception as e:
        return False
    return True
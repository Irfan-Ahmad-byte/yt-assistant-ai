from app.workers.prepare_graph import graph
# a function to store transcpit into neo4j with id as reference

def store_transcript(id, text):
    response = graph.query (
        f"""
        CREATE (t:Transcript {{id: {id}, text: "{text}"}})
        RETURN t
        """
    )

    return response

# a fucntion to get the transcipt from neo4j with id as reference

def get_transcript(id):
    response = graph.query (
        f"""
        MATCH (t:Transcript {{id: {id}}})
        RETURN t.text
        """
    )

    return response
from app.executors.chain import create_qa_chain
from app.executors.vector_store import create_neo4j_vector_store
from app.workers.manage_transcript import get_transcript



dummy_answer = "I am a dummy answer. I am not sure how to answer your question. Please ask me something else."

def get_answer(id, query: str, callbacks: list = None):
    print("Getting user's transcript..............")
    docs = get_transcript(id)
    print("Creating vector store..............")
    vectorstore = create_neo4j_vector_store(id, docs)
    print("Creating QA chain..................")
    qa_chain = create_qa_chain(vectorstore)
    print("Asking the QA chain................")
    for chunk in qa_chain.stream({"input":query}, config={"callbacks": callbacks}):
        yield chunk

        
# def get_answer(query: str, callbacks: list = None):
#     for chunk in dummy_answer:
#         time.sleep(0.20)
#         yield chunk
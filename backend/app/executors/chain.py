from langchain.chains.combine_documents import create_stuff_documents_chain
from app.executors.retriever import CustomRetriever
from langchain.chains.retrieval import create_retrieval_chain
from langchain_community.vectorstores.neo4j_vector import Neo4jVector
from langchain import hub

from app.utils.llm import get_llm


def create_qa_chain(vectorstore: Neo4jVector):
    retrieval_qa_chat_prompt = hub.pull("langchain-ai/retrieval-qa-chat")

    custom_retriever = CustomRetriever(vectorstore=vectorstore)

    # Create an LLM for answering questions
    llm = get_llm()

    combine_docs_chain = create_stuff_documents_chain(
        llm, retrieval_qa_chat_prompt
    )

    # Create the RetrievalQA chain with the custom retriever
    qa_chain = create_retrieval_chain(
        custom_retriever,
        combine_docs_chain
    )
    
    return qa_chain
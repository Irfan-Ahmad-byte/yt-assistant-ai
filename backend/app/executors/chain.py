
from langchain_openai import ChatOpenAI
from app.config.config import Config
from app.executors.vector_store import create_neo4j_vector_store
from langchain.chains.combine_documents import create_stuff_documents_chain
from app.executors.retriever import CustomRetriever
from langchain.chains.retrieval import create_retrieval_chain
from langchain import hub


retrieval_qa_chat_prompt = hub.pull("langchain-ai/retrieval-qa-chat")

vectorstore = create_neo4j_vector_store()
custom_retriever = CustomRetriever(vectorstore=vectorstore)

# Create an LLM for answering questions
llm = ChatOpenAI(temperature=0, model_name=Config.MODEL, openai_api_key=Config.OPENAI_API_KEY)

combine_docs_chain = create_stuff_documents_chain(
    llm, retrieval_qa_chat_prompt
)

# Create the RetrievalQA chain with the custom retriever
qa_chain = create_retrieval_chain(
    custom_retriever,
    combine_docs_chain
)
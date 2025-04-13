import threading

from langchain_text_splitters import RecursiveCharacterTextSplitter
from app.config.config import Config
from langchain_community.vectorstores.neo4j_vector import Neo4jVector
from langchain.docstore.document import Document
from langchain_openai import OpenAIEmbeddings
from typing import List

from app.utils.llm import get_llm



def load_documents(vectorstore:Neo4jVector, doc: str) -> List[Document]:
    embeddings = OpenAIEmbeddings(openai_api_key=Config.OPENAI_API_KEY)
    docs = vectorstore.from_documents(doc, embeddings)
    return docs


def split_docs(docs: List[Document]):
    '''
        function to split documents into sentences

        params:
            docs: List of Doc objects

        returns:
            List of Doc objects
    '''

    #initialize the splitter
    splitter = RecursiveCharacterTextSplitter(chunk_size=512, chunk_overlap=24)
    #split the documents
    docs = splitter.split_documents(docs)
    print('Splitting complete')
    #return the split documents
    return docs


# def split_into_graph(docs: List[Document]):
#     print('Converting to graph documents...')
#     llm = get_llm()
#     llm_transformer = LLMGraphTransformer(llm=llm, prompt=nodes_prompt)
    
#     # Create a queue to store the results from each thread
#     result_queue = Queue()
    
#     # num of threads
#     num_threads = min(len(docs), threading.active_count())

#     try:
#         # Define the target function for each thread
#         def process_chunk(chunk):
#             result_queue.put(llm_transformer.convert_to_graph_documents(chunk))

#         # Create and start threads
#         threads = []
#         chunk_size = len(docs) // num_threads
#         for i in range(num_threads):
#             start_idx = i * chunk_size
#             end_idx = start_idx + chunk_size if i < num_threads - 1 else len(docs)
#             chunk = docs[start_idx:end_idx]
#             t = threading.Thread(target=process_chunk, args=(chunk,))
#             t.start()
#             threads.append(t)

#         # Wait for all threads to finish
#         for t in threads:
#             t.join()

#         # Collect results from the queue
#         graph_documents = []
#         while not result_queue.empty():
#             graph_documents.extend(result_queue.get())

#     except Exception as e:
#         print(f"Error converting to graph documents: {e}")
#         raise e

#     print('Conversion to graph documents complete...')
#     return graph_documents
# from app.executors.chain import qa_chain


import time


dummy_answer = "I am a dummy answer. I am not sure how to answer your question. Please ask me something else."

# def get_answer(query: str, callbacks: list = None):
#     for chunk in qa_chain.stream({"question":query}, config={"callbacks": callbacks}):
#         yield chunk

        
def get_answer(query: str, callbacks: list = None):
    for chunk in dummy_answer:
        time.sleep(0.20)
        yield chunk
# script to test my api app functions
from app.config.config import Config
from app.executors.agent import get_answer


if __name__ == "__main__":

    # Test the agent endpoint
    print("Testing agent endpoint")

    response = ""
    for r in get_answer(1231, Config.TEST_QUERY, Config.TEST_DOC):
        response += r

    print(response)
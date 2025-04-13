from typing import List
from llama_index_client import Document
from llama_parse import LlamaParse, ResultType
import nest_asyncio

from config.config import Config

def parse(path:str) -> List[Document]:
    nest_asyncio.apply()
    parser = LlamaParse(
        api_key=Config.LLAMA_CLOUD_API_KEY,
        num_workers=4, # if multiple files passed, split in `num_workers` API calls
        language="en",
        verbose=True,
        result_type=ResultType.MD,
    )

    documents = parser.load_data(path)

    return documents
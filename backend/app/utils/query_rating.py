
from pydantic import BaseModel, Field


class RatingScore(BaseModel):
    relevance_score: float = Field(..., description="The relevance score of a document to a query.")

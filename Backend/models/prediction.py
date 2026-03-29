from pydantic import BaseModel
from typing import List

class Prediction(BaseModel):
    user_id: str   # store MongoDB ObjectId as string
    input_data: List[float]
    result: int
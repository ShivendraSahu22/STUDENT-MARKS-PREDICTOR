from pydantic import BaseModel, Field
from typing import Dict

class PredictionResponse(BaseModel):
    predicted_marks: float = Field(
        ...,
        description="The predicted student marks"
    )
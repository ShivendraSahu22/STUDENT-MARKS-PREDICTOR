from pydantic import BaseModel, Field, field_validator
from typing import Annotated, Literal



class UserInput(BaseModel):

     'number_courses': Annotated[int, Field(..., description="Number of courses taken by the student")]
     'time_study': Annotated[float, Field(..., description="Time spent studying")]
from typing import Optional
from pydantic import BaseModel, EmailStr, Field

# schema to store a studen

# base student model for creation
class StudentSchema(BaseModel):
    fullname : str = Field(...) # ... = required ; none or defaul value
    email: EmailStr = Field(...)
    course_of_study: str = Field(...)
    year: int = Field(..., gt=0, lt=9) # gt, lt = greater than, lower than
    gpa: float = Field(..., le=4.0) # le = less or equals

    # config for doc
    class Config:
        schema_extra = {
            "example": {
                "fullname": "John Doe",
                "email": "jdoe@x.edu.ng",
                "course_of_study": "Water resources engineering",
                "year": 2,
                "gpa": "3.0",
            }
        }

# base student model for updating
class UpdateStudentModel(BaseModel):
    fullname: Optional[str] # all values are optional
    email: Optional[EmailStr]
    course_of_study: Optional[str]
    year: Optional[int]
    gpa: Optional[float]

    class Config:
        schema_extra = {
            "example": {
                "fullname": "John Doe",
                "email": "jdoe@x.edu.ng",
                "course_of_study": "Water resources and environmental engineering",
                "year": 4,
                "gpa": "4.0",
            }
        }

# basic response
def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }

# basic error
def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
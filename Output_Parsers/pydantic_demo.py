from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name: str
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0, lt=0)


# you can't pass the Number as string string will be string and number will be number
new_student = {'age':32, 'email':'abac@gmail.com'}

student = Student(**new_student)
print(student)
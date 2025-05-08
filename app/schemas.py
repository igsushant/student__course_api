from typing import List, Optional
from pydantic import BaseModel, EmailStr
from datetime import datetime

class StudentCreate(BaseModel):
    name: str
    email: EmailStr

class CourseCreate(BaseModel):
    title: str
    description: Optional[str] = None

class StudentOut(BaseModel):
    id: int
    name: str
    email: EmailStr
    courses: List['CourseOut'] = []

    class Config:
        orm_mode = True

class CourseOut(BaseModel):
    id: int
    title: str
    description: Optional[str]
    students: List['StudentOut'] = []

    class Config:
        orm_mode = True

class EnrollmentRequest(BaseModel):
    student_id: int
    course_id: int

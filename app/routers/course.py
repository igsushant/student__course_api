from fastapi import APIRouter

router = APIRouter()

@router.post("/courses/")
def create_course():
    return {"message": "Course created"}

@router.get("/courses/{id}")
def get_course(id: int):
    return {"id": id, "title": "Sample Course"}
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas, database

router = APIRouter()

@router.post("/courses/", response_model=schemas.CourseOut)
def create_course(course: schemas.CourseCreate, db: Session = Depends(database.SessionLocal)):
    return crud.create_course(db, course)

@router.get("/courses/{id}", response_model=schemas.CourseOut)
def get_course(id: int, db: Session = Depends(database.SessionLocal)):
    course = crud.get_course(db, id)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course

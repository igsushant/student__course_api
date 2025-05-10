from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import crud, schemas, database, models

router = APIRouter()

@router.post("/courses/", response_model=schemas.CourseOut)
def create_course(course: schemas.CourseCreate, db: Session = Depends(database.get_db)):
    return crud.create_course(db, course)

@router.get("/courses/{id}", response_model=schemas.CourseOut)
def get_course(id: int, db: Session = Depends(database.get_db)):
    course = crud.get_course(db, id)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course

# New endpoint to list courses with pagination
@router.get("/courses/", response_model=List[schemas.CourseOut])
def list_courses(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    courses = db.query(models.Course).offset(skip).limit(limit).all()
    return courses

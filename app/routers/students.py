from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import crud, schemas, database, models

router = APIRouter()

@router.post("/students/", response_model=schemas.StudentOut)
def create_student(student: schemas.StudentCreate, db: Session = Depends(database.get_db)):
    return crud.create_student(db, student)

@router.get("/students/{id}", response_model=schemas.StudentOut)
def get_student(id: int, db: Session = Depends(database.get_db)):
    student = crud.get_student(db, id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

# New endpoint to list students with pagination
@router.get("/students/", response_model=List[schemas.StudentOut])
def list_students(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    students = db.query(models.Student).offset(skip).limit(limit).all()
    return students

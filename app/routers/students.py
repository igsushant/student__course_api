from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas, database


router = APIRouter()

@router.post("/students/", response_model=schemas.StudentOut)
def create_student(student: schemas.StudentCreate, db: Session = Depends(database.SessionLocal)):
    return crud.create_student(db, student)

@router.get("/students/{id}", response_model=schemas.StudentOut)
def get_student(id: int, db: Session = Depends(database.SessionLocal)):
    student = crud.get_student(db, id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

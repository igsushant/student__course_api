from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas, database

router = APIRouter()

@router.post("/enroll/")
def enroll(req: schemas.EnrollmentRequest, db: Session = Depends(database.SessionLocal)):
    success = crud.enroll_student(db, req.student_id, req.course_id)
    if not success:
        raise HTTPException(status_code=400, detail="Enrollment failed")
    return {"message": "Enrollment successful"}

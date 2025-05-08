from sqlalchemy.orm import Session
from app import models, schemas


def create_student(db: Session, student: schemas.StudentCreate):
    db_student = models.Student(**student.dict())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def create_course(db: Session, course: schemas.CourseCreate):
    db_course = models.Course(**course.dict())
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course

def enroll_student(db: Session, student_id: int, course_id: int):
    student = db.query(models.Student).get(student_id)
    course = db.query(models.Course).get(course_id)
    if student and course:
        student.courses.append(course)
        db.commit()
        return True
    return False

def get_student(db: Session, student_id: int):
    return db.query(models.Student).filter(models.Student.id == student_id).first()

def get_course(db: Session, course_id: int):
    return db.query(models.Course).filter(models.Course.id == course_id).first()

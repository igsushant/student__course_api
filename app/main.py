from fastapi import FastAPI
from app.database import Base, engine
from app.routers import students, course, enrollments

# Create database tables
Base.metadata.create_all(bind=engine)

# Initialize app
app = FastAPI()

# Register routes
app.include_router(students.router)
app.include_router(course.router)
app.include_router(enrollments.router)

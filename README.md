##Student Course Management API
This is a minimal REST API to manage students and their enrolled courses. Built with FastAPI, SQLAlchemy, and Pydantic, it supports core CRUD operations and student-course enrollment logic.

##Features:
Create and retrieve students and courses
Enroll students in courses
View student details with enrolled courses
View course details with enrolled students
Pydantic-based request validation (with email validation)
Database ORM with SQLAlchemy
Auto-generated interactive API docs at /docs



## Getting Started

### Clone the Repository

```bash
git clone https://github.com/igsushant/student__course_api.git
cd student__course_api
```

Install Dependencies:
Make sure you have Python 3.7 or higher installed.
Install the requirements from requirements.txt 

Run the app:
uvicorn app.main:app --reload(Run it in terminal)

Open in browser(Paste the url):
Swagger UI: http://127.0.0.1:8000/docs
ReDoc: http://127.0.0.1:8000/redoc

Tech Stack:
FastAPI – API framework
Pydantic – Data validation
SQLAlchemy – ORM
SQLite – Default database (can be changed)

# Student-Course API

This is a FastAPI-based backend project for managing students and courses. It includes RESTful endpoints with auto-generated documentation.

## Features

- Create, read, update, and delete students and courses
- Swagger UI documentation at `/docs`
- Modular and clean code structure


## Getting Started

### Clone the Repository

```bash
git clone https://github.com/igsushant/student__course_api.git
cd student__course_api
```

Install Dependencies
Make sure you have Python 3.7 or higher installed.
pip install -r requirements.txt

Run the Server
uvicorn main:app --reload

Access the API Docs:
Swagger UI: http://127.0.0.1:8000/docs
ReDoc: http://127.0.0.1:8000/redoc

Tech Stack:
FastAPI – API framework
Pydantic – Data validation
SQLAlchemy – ORM
SQLite – Default database (can be changed)

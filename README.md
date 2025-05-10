# Student Course Management API

This is a minimal REST API to manage students and their enrolled courses. Built with **FastAPI**, **SQLAlchemy**, and **Pydantic**, it supports core CRUD operations and student-course enrollment logic.

---

## 🚀 Features

- Create and retrieve **students** and **courses**
- Enroll students in courses
- View student details with enrolled courses
- View course details with enrolled students
- Email field validation
- Pagination support for list APIs
- Basic unit testing using `pytest`
- Auto-generated interactive API docs at `/docs`

---

## 🧱 Technologies Used

- FastAPI – API framework  
- Pydantic – Data validation  
- SQLAlchemy – ORM  
- SQLite – Default database (can be changed to PostgreSQL)  
- Uvicorn – ASGI server  
- Pytest – For testing  

---

## ⚙️ Getting Started

### Clone the Repository

```bash
git clone https://github.com/igsushant/student__course_api.git
cd student__course_api
```
Install Dependencies: Make sure you have Python 3.7 or higher installed. 
Install the requirements listed in requirements.txt

Run the FastAPI application using uvicorn:
uvicorn app.main:app --reload
This will start the server on http://127.0.0.1:8000.

Open API Documentation

Once the app is running, you can access the interactive API documentation in your browser:
Swagger UI: http://127.0.0.1:8000/docs
ReDoc: http://127.0.0.1:8000/redoc

📬 API Testing  
You can test the API using Swagger UI, ReDoc, or via cURL commands.

➡️ [See full list of sample cURL commands](https://github.com/igsushant/student__course_api/blob/master/sample_curls.md)

 Running Unit Tests
Basic unit tests are available in test_main.py.

To run the tests:
pytest test_main.py






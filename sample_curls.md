# Sample cURL Commands to Test API Endpoints

These are sample cURL commands you can use to test the Student Course Management API.

---

## 1. Create a Student
This command creates a new student.

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/students/' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "John Doe",
  "email": "john.doe@example.com"
}'

Expected response:
{
  "id": 1,
  "name": "John Doe",
  "email": "john.doe@example.com",
  "courses": []
}

2. Create a Course
curl -X 'POST' \
  'http://127.0.0.1:8000/courses/' \
  -H 'Content-Type: application/json' \
  -d '{
  "title": "Math 101",
  "description": "Introduction to Math"
}'

Expected Response:
{
  "id": 1,
  "title": "Math 101",
  "description": "Introduction to Math"
}

3. List Students (with Pagination)
curl -X 'GET' \
  'http://127.0.0.1:8000/students/?skip=0&limit=5'

Expected Response:
[
  {
    "id": 1,
    "name": "John Doe",
    "email": "john.doe@example.com",
    "courses": []
  }
]

4. List Courses (with Pagination)
curl -X 'GET' \
  'http://127.0.0.1:8000/courses/?skip=0&limit=5'

Expected Response:
[
  {
    "id": 1,
    "title": "Math 101",
    "description": "Introduction to Math",
    "students": []
  }
]
5. Enroll a Student in a Course
curl -X 'POST' \
  'http://127.0.0.1:8000/enroll/' \
  -H 'Content-Type: application/json' \
  -d '{
  "student_id": 1,
  "course_id": 1
}'

Expected Response:
{
  "message": "Enrollment successful"
}

```

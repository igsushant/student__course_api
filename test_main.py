from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_student():
    response = client.post("/students/", json={"name": "Test User", "email": "testuser@example.com"})
    assert response.status_code == 200
    assert response.json()["name"] == "Test User"
    assert response.json()["email"] == "testuser@example.com"

def test_create_course():
    response = client.post("/courses/", json={"title": "Test Course", "description": "Test Description"})
    assert response.status_code == 200
    assert response.json()["title"] == "Test Course"

def test_enroll_student():
    student = client.post("/students/", json={"name": "Enroll User", "email": "enrolluser@example.com"}).json()
    course = client.post("/courses/", json={"title": "Enroll Course", "description": "Enroll Desc"}).json()
    enroll_response = client.post("/enroll/", json={"student_id": student["id"], "course_id": course["id"]})
    assert enroll_response.status_code == 200
    assert enroll_response.json()["message"] == "Enrollment successful"

def test_get_student():
    student = client.post("/students/", json={"name": "Get User", "email": "getuser@example.com"}).json()
    response = client.get(f"/students/{student['id']}")
    assert response.status_code == 200
    assert response.json()["name"] == "Get User"

def test_get_course():
    course = client.post("/courses/", json={"title": "Get Course", "description": "Get Desc"}).json()
    response = client.get(f"/courses/{course['id']}")
    assert response.status_code == 200
    assert response.json()["title"] == "Get Course"

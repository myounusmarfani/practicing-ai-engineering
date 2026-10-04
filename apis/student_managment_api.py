"""
🔹 1. Smart Student Management API

Level: Beginner → Intermediate  

What to Build
- CRUD API (create, read, update, delete students)
- Store data in database
- Add filtering (top students, failed students)

Skills You Use
- FastAPI
- Database (Json files or Lists)
- JSON handling

Upgrade Idea
- Add analytics (average marks, charts)

"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

students = []

app = FastAPI(
    title="Smart Student Management API",
    description="A simple API to manage student records with CRUD operations and filtering capabilities.",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Student(BaseModel):
    id: int
    name: str
    age: int
    marks: float

# CRUD Operations

# Create a new student

@app.post("/students/", response_model=Student)
def create_student(student: Student):
    for existing_student in students:
        if existing_student.id == student.id:
            raise HTTPException(status_code=400, detail="Student with this ID already exists.")
    students.append(student)
    return student

# Read all students

@app.get("/students/", response_model=list[Student])
def read_students():
    return students

# Read a student by ID

@app.get("/students/{student_id}", response_model=Student)
def read_student(student_id: int):
    for student in students:
        if student.id == student_id:
            return student
    raise HTTPException(status_code=404, detail="Student not found.")

# Update a student by ID
@app.put("/students/{student_id}", response_model=Student)
def update_student(student_id: int, updated_student: Student):
    for index, student in enumerate(students):
        if student.id == student_id:
            students[index] = updated_student
            return updated_student
    raise HTTPException(status_code=404, detail="Student not found.")

# Delete a student by ID
@app.delete("/students/{student_id}", response_model=Student)
def delete_student(student_id: int):
    for index, student in enumerate(students):
        if student.id == student_id:
            return students.pop(index)
    raise HTTPException(status_code=404, detail="Student not found.")

# Filtering Operations
@app.get("/students/top", response_model=list[Student])
def get_top_students():
    top_students = sorted(students, key=lambda x: x.marks, reverse=True)[:5]
    return top_students

# Get failed students (marks < 40)
@app.get("/students/failed", response_model=list[Student])
def get_failed_students():
    failed_students = [student for student in students if student.marks < 40]
    return failed_students

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)


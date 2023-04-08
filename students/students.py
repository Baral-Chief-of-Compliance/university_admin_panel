from flask import Blueprint, jsonify
from app.useDB import students_db

students = Blueprint('students', __name__)


@students.route('/')
def all_students():
    students = students_db.all_students()
    print(students)
    return jsonify({
        "students": students
    })
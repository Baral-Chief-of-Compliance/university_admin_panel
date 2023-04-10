from app import app, jsonify, request
from students.students import students
from teacher.teacher import teacher
from disciplines.disciplines import disciplines
from form_of_work.form_of_work import forms_of_work


app.register_blueprint(students, url_prefix='/students')
app.register_blueprint(teacher, url_prefix='/teachers')
app.register_blueprint(disciplines, url_prefix='/disciplines')
app.register_blueprint(forms_of_work, url_prefix='/forms_of_work')

@app.route('/')
def hello():
    return "hello world"
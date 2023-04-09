from app import app, jsonify, request
from students.students import students
from teacher.teacher import teacher


app.register_blueprint(students, url_prefix='/students')
app.register_blueprint(teacher, url_prefix='/teachers')

@app.route('/')
def hello():
    return "hello world"
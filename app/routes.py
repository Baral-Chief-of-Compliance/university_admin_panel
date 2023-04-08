from app import app, jsonify, request
from students.students import students


app.register_blueprint(students, url_prefix='/students')

@app.route('/')
def hello():
    return "hello world"
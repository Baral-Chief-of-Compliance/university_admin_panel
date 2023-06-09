from flask import Blueprint, request, jsonify
from app.useDB import teachers_db
from app.useDB import workload_db


teacher = Blueprint('teachers', __name__)


@teacher.route("/all", methods=["GET", "POST"])
def all_teacher():
    if request.method == "GET":
        json_teachers = []
        all_teachers = teachers_db.all_teachers()

        for t in all_teachers:
            json_teachers.append({
                "num_t": t[0],
                "surname_t": t[1],
                "name_t": t[2],
                "patri_t": t[3],
                "post": t[4]
            })
        return jsonify(json_teachers)

    elif request.method == "POST":
        surname_t = request.json["surname_t"]
        name_t = request.json["name_t"]
        patri_t = request.json["patri_t"]
        post = request.json["post"]

        teachers_db.create_teacher([surname_t,
                                    name_t,
                                    patri_t,
                                    post])

        return jsonify(f"teacher {surname_t} {name_t} is add")


@teacher.route("/<int:num_t>", methods=["GET", "DELETE"])
def inf_about_teacher(num_t):
    if request.method == "GET":
        json_workload = []
        inf = teachers_db.inf_about_teacher(num_t)
        workload = workload_db.workload_for_teacher(num_t)

        for w in workload:
            json_workload.append({
                "course": w[0],
                "semester": w[1],
                "type_of_classes": w[2],
                "hours": w[3],
                "name_control": w[4],
                "name_dis": w[5]
            })

        return jsonify({
            "num_t": inf[0],
            "surname_t": inf[1],
            "name_t": inf[2],
            "patri_t": inf[3],
            "post": inf[4],
            "workload": json_workload
        })

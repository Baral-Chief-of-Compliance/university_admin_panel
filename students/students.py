from flask import Blueprint, jsonify, request
from app.useDB import students_db
from app.useDB import delivery_of_work_db

students = Blueprint('students', __name__)


@students.route('/all', methods=["GET", "POST"])
def all_students():
    if request.method == "GET":
        json_students = []
        all_students = students_db.all_students()

        for std in all_students:
            json_students.append({
                "num_credit": std[0],
                "surname_s": std[1],
                "name_s": std[2],
                "patro_s": std[3],
                "num_group": std[4],
                "year_of_admission": std[5]
            })

        return jsonify(json_students)

    elif request.method == "POST":
        num_credit = request.json["num_credit"]
        surname_s = request.json["surname_s"]
        name_s = request.json["name_s"]
        patro_s = request.json["patro_s"]
        num_group = request.json["num_group"]
        year_of_admission = request.json["year_of_admission"]

        students_db.create_student([num_credit, surname_s,
                                    name_s, patro_s,
                                    num_group, year_of_admission])

        return jsonify(f"students {num_credit} is add")


@students.route("/<int:num_credit>", methods=["GET", "DELETE"])
def inf_about_student(num_credit):
    if request.method == "GET":
        json_delivery = []
        inf = students_db.inf_about_student(num_credit)
        delivery = delivery_of_work_db.delivery_for_student(num_credit)

        for d in delivery:
            json_delivery.append({
                "score": d[0],
                "date_work": d[1],
                "name_w": d[2],
                "name_control": d[3],
                "name_dis": d[4]
            })

        return jsonify({
            "num_credit": inf[0],
            "surname_s": inf[1],
            "name_s": inf[2],
            "patro_s": inf[3],
            "num_group": inf[4],
            "year_of_admission": inf[5],
            "delivery": json_delivery
        })

    elif request.method == "DELETE":
        students_db.delete_student(num_credit)

        return jsonify(f"delete student {num_credit}")


from flask import Blueprint, jsonify, request
from app.useDB import disciplines_db
from app.useDB import form_of_work_db


disciplines = Blueprint('disciplines', __name__)


@disciplines.route('/all', methods=["GET", "POST"])
def all_disciplines():
    if request.method == "GET":
        json_disciplines = []
        all_disciplines = disciplines_db.all_disciplines()

        for d in all_disciplines:
            json_disciplines.append({
                "num_dis": d[0],
                "name_dis": d[1]
            })

        return jsonify(json_disciplines)

    elif request.method == "POST":
        name_dis = request.json["name_dis"]

        disciplines_db.create_discipline([name_dis])

        return jsonify(f"discipline {name_dis} is add")


@disciplines.route("/<int:num_dis>", methods=["GET", "DELETE"])
def inf_about_discipline(num_dis):
    if request.method == "GET":
        json_forms_of_work = []
        inf = disciplines_db.inf_about_discipline(num_dis)
        inf_about_work = form_of_work_db.forms_for_discipline(num_dis)

        for i in inf_about_work:
            json_forms_of_work.append({
                "num_work": i[0],
                "num_dis": i[1],
                "name_control": i[2]
            })

        return jsonify({
            "num_dis": inf[0],
            "name_dis": inf[1],
            "forms_of_work": json_forms_of_work
        })

    elif request.method == "DELETE":
        disciplines_db.delete_discipline(num_dis)

        return jsonify(f"discipline {num_dis} is delete")

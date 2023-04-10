from flask import Blueprint, jsonify, request
from app.useDB import disciplines_db


disciplines = Blueprint('disciplines', __name__)


@disciplines.route('/', methods=["GET", "POST"])
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
        inf = disciplines_db.inf_about_discipline(num_dis)

        return jsonify({
            "num_dis": inf[0],
            "name_dis": inf[1]
        })

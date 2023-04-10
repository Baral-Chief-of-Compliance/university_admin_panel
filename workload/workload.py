from flask import Blueprint, jsonify, request
from app.useDB import workload_db

workload = Blueprint('workload', __name__)


@workload.route('/', methods=["POST"])
def all_workload():
    if request.method == "POST":
        num_t = request.json["num_t"]
        num_work = request.json["num_work"]
        course = request.json["course"]
        semester = request.json["semester"]
        type_of_classes = request.json["type_of_classes"]
        hours = request.json["hours"]

        workload_db.create_workload([num_t, num_work, course,
                                     semester, type_of_classes, hours])

        return jsonify(f"workload {type_of_classes} add for {num_work}")

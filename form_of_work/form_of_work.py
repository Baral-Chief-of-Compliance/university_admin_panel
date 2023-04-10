from flask import Blueprint, jsonify, request
from app.useDB import form_of_work_db


forms_of_work = Blueprint('forms_of_work', __name__)


@forms_of_work.route('/', methods=["POST"])
def all_forms():
    if request.method == "POST":
        num_dis = request.json["num_dis"]
        name_control = request.json["name_control"]

        form_of_work_db.create_form([num_dis, name_control])

        return jsonify(f"{name_control} for {num_dis} is add")


from flask import Blueprint, jsonify, request
from app.useDB import delivery_of_work_db

delivery_of_work = Blueprint('delivery_of_work', __name__)


@delivery_of_work.route('/', methods=["POST"])
def all_delivery():
    if request.method == "POST":
        num_credit = request.json["num_credit"]
        num_work = request.json["num_work"]
        score = request.json["score"]
        date_work = request.json["date_work"]
        name_w = request.json["name_w"]

        delivery_of_work_db.create_delivery_of_work([num_credit,
                                                     num_work,
                                                     score,
                                                     date_work,
                                                     name_w])

        return jsonify(f"delivery_of_work of {num_work} for {num_credit} is add")


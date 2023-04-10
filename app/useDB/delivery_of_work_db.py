from app.useDB.tools import quarry


def create_delivery_of_work(*args):
    quarry.call("insert into delivery_of_work values "
                "(%s, %s, %s, %s, %s)", *args,
                commit=True, fetchall=False)


def delivery_for_student(num_credit):
    delivery = quarry.call("select delivery_of_work.score, "
                           "delivery_of_work.date_work, "
                           "delivery_of_work.name_w, "
                           "form_of_work.name_control, "
                           "discipline.name_dis from "
                           "delivery_of_work "
                           "inner join form_of_work "
                           "on delivery_of_work.num_work = form_of_work.num_work "
                           "inner join discipline "
                           "on form_of_work.num_dis = discipline.num_dis "
                           "where num_credit = %s",
                           [num_credit], commit=False, fetchall=True)

    return delivery

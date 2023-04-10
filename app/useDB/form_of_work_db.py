from app.useDB.tools import quarry


def create_form(*args):
    quarry.call("insert into form_of_work(num_dis, name_control) values "
                "(%s, %s)", *args, commit=True, fetchall=False)


def forms_for_discipline(num_dis):
    forms = quarry.call("select * from form_of_work where num_dis = %s",
                        [num_dis], commit=False, fetchall=True)

    return forms

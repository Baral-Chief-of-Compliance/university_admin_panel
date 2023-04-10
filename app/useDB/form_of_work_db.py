from app.useDB.tools import quarry


def create_form(*args):
    quarry.call("insert into form_of_work(num_dis, name_control) values "
                "(%s, %s)", *args, commit=True, fetchall=False)

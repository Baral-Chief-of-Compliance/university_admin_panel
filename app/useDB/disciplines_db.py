from app.useDB.tools import quarry


def all_disciplines():
    disciplines = quarry.call("select * from discipline", commit=False, fetchall=True)
    return disciplines


def create_discipline(*args):
    quarry.call("insert into discipline(name_dis) "
                "values (%s)", *args, commit=True, fetchall=False)


def inf_about_discipline(num_dis):
    inf = quarry.call("select * from discipline where num_dis = %s",
                      [num_dis],
                      commit=False, fetchall=False)

    return inf


def delete_discipline(num_dis):
    quarry.call("delete from discipline where num_dis = %s",
                [num_dis],
                commit=True, fetchall=False)

from app.useDB.tools import quarry


def all_teachers():
    teachers = quarry.call("select * from teacher", commit=False, fetchall=True)
    return teachers


def create_teacher(*args):
    quarry.call("insert into teacher(surname_t, name_t, patri_t, post) values "
                "(%s, %s, %s, %s)", *args, commit=True, fetchall=False)


def inf_about_teacher(num_t):
    inf = quarry.call("select * from teacher where num_t = %s",
                      [num_t],
                      commit=False, fetchall=False)

    return inf

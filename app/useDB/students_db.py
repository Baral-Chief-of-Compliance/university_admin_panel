from app.useDB.tools import quarry


def all_students():
   students = quarry.call("select * from student", commit=False, fetchall=True)
   return students


def create_student(*args):
   quarry.call("insert into student values "
               "(%s, %s, %s, %s, %s, %s)", *args, commit=True, fetchall=False)


def inf_about_student(num_credit):
    inf = quarry.call("select * from student where num_credit = %s",
                      [num_credit],
                      commit=False, fetchall=False)

    return inf


def delete_student(num_credit):
    quarry.call("DELETE FROM student where num_credit = %s",
                [num_credit], commit=True, fetchall=False)

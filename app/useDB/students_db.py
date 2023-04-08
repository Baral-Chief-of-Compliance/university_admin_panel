from app.useDB.tools import quarry


def all_students():
   students = quarry.call("select * from student", commit=False, fetchall=True)
   return students
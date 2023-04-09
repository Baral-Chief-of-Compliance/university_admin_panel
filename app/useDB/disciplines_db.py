from app.useDB.tools import quarry


def all_disciplines():
    disciplines = quarry.call("select * from discipline", commit=False, fetchall=True)
    return disciplines
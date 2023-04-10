from app.useDB.tools import quarry


def create_workload(*args):
    quarry.call("insert into workload values "
                "(%s, %s, %s, %s, %s, %s)", *args,
                commit=True, fetchall=False)


def workload_for_teacher(num_t):
    workload = quarry.call("select workload.course, workload.semester, "
                           "workload.type_of_classes, workload.hours, "
                           "form_of_work.name_control, discipline.name_dis "
                           "from workload "
                           "inner join form_of_work "
                           "on workload.num_work = form_of_work.num_work "
                           "inner join discipline "
                           "on form_of_work.num_dis = discipline.num_dis "
                           "where num_t = %s",
                           [num_t], commit=False, fetchall=True)

    return workload

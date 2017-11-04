from sprint.models import Sprint
from project.models import *
from datetime import datetime, timedelta



def genrate_sprint(pbs, sprint_length, end_date):
    start_date = pbs.start_date
    i=1
    while start_date < pbs.ETA:
        s1 = Sprint()
        s1.start_date = start_date
        s1.end_date = start_date + timedelta(sprint_length)
        s1.project_backlog = pbs
        s1.name = pbs.projectBacklogSetting.sprint_template + str(i)
        i+=1
        s1.save()
        start_date = s1.end_date+timedelta(1)



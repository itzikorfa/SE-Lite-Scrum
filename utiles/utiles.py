from sprint.models import Sprint
from project.models import *
from datetime import datetime, timedelta
from covey.models import CoveyMatrix
from project.models import TaskStages
from meeting.models import MeetingType



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
    add_data_to_project()


def load_data_covey():
    c1 = CoveyMatrix(name="important , urgent")
    c1.save()
    c1 = CoveyMatrix(name="important , not urgent")
    c1.save()
    c1 = CoveyMatrix(name="not important , urgent")
    c1.save()
    c1 = CoveyMatrix(name="not important , not urgent")
    c1.save()

def load_data_taskstage():
    t1 = TaskStages(stage=1,stage_name="Learn")
    t1.save()
    t1 = TaskStages(stage=2, stage_name="plan")
    t1.save()
    t1 = TaskStages(stage=3 ,stage_name="Design")
    t1.save()
    t1 = TaskStages(stage=4, stage_name="solve")
    t1.save()
    t1 = TaskStages(stage=5,stage_name="review")
    t1.save()

def load_data_MeetingType():

    c1 = MeetingType(name="Daily")
    c1.save()
    c1 = MeetingType(name="Weekly")
    c1.save()
    c1 = MeetingType(name="Sprint Planning")
    c1.save()
    c1 = MeetingType(name="Sprint Review Meeting")
    c1.save()


def add_data_to_project():
    temp = CoveyMatrix.objects.all()
    if len(temp) == 0:
        load_data_covey()
    temp = TaskStages.objects.all()
    if len(temp) == 0:
        load_data_taskstage()
    temp = MeetingType.objects.all()
    if len(temp) == 0:
        load_data_MeetingType()

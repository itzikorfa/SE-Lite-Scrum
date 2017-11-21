from sprint.models import Sprint
from project.models import *
from datetime import datetime, timedelta
from covey.models import CoveyMatrix
from project.models import TaskStages
from meeting.models import MeetingType
from task.models import Task, TaskProperty
from accounts.models import User
from groups.models import Group
from django.shortcuts import get_object_or_404
from django.conf import settings
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


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


def create_covey_graph(team=-1, user=1):
    if team>=0:
        query = Task.objects.filter(team=team)
    else:
        query = Task.objects.filter(taskProperty__assign_to=user)
    data = dict()
    for i in query:
        if i.task_type in data:
            data[i.task_type]+=1
        else:
            data[i.task_type]=1


    keys = list()
    value = list()

    for key in data:
        keys.append(key)
        value.append(data[key])

    plt.pie([float(v) for v in value], labels=[k for k in keys],
               autopct=None)

    if team>0:
        team_name = get_object_or_404(Group, pk=team).name
        file_name = str(user)+"_group"+".png"
    else:

        file_name = str(user)+"_user"+".png"
    plt.savefig(os.path.join(settings.MEDIA_ROOT,file_name))
    return data, file_name


def analayes_covey_data(data):
    if ('important , urgent' in  data):
        pass

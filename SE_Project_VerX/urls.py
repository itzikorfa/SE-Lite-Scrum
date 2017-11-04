from django.conf.urls import url,include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r"^$", views.HomePage.as_view(), name="home"),
    url(r"^index/$", views.TestPage.as_view(), name="test"),
    url(r"^thanks/$", views.ThanksPage.as_view(), name="thanks"),
    url(r'^admin/', admin.site.urls, name='admin'),
    url(r"^accounts/", include("accounts.urls", namespace="accounts")),
    url(r"^accounts/", include("django.contrib.auth.urls")),
    url(r"^groups/",include("groups.urls", namespace="groups")),
    url(r'^company/', include('company.urls',namespace='company')),
    url(r'^project/', include('project.urls',namespace='project')),
    url(r'^sprint/', include('sprint.urls',namespace='sprint')),
    url(r'^task/', include('task.urls',namespace='task')),
    url(r'^log/', include('log.urls',namespace='log')),
    url(r'^todo/', include('todo.urls',namespace='todo')),


]

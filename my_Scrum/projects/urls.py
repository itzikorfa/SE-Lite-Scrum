from django.conf.urls import url

from . import views

app_name = 'projects'

urlpatterns = [
    url(r"^$", views.ProjectsList.as_view(), name="all"),
    url(r"^(?P<pk>[-\w]+)/$", views.ProjectsDetail.as_view(), name="single"),
    # url(r"^new/$", views.ProjectsCreate.as_view(), name="create"),
    # url(r"^update/(?P<pk>\d+)/$",views.ProjectsUpdate.as_view(), name="update")
]

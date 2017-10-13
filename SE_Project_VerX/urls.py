from django.conf.urls import url,include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r"^$", views.HomePage.as_view(), name="home"),
    url(r"^test/$", views.TestPage.as_view(), name="test"),
    url(r"^thanks/$", views.ThanksPage.as_view(), name="thanks"),
    url(r'^admin/', admin.site.urls),
    url(r"^groups/",include("groups.urls", namespace="groups")),
    url(r'^company/', include('company.urls',namespace='company')),
    url(r'^project/', include('project.urls',namespace='project')),

]
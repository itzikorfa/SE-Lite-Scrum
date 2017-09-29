from django.conf.urls import url

from . import views

app_name = 'company'

urlpatterns = [
    url(r"^$", views.ListCompanys.as_view(), name="all"),
    url(r"^new/$", views.CreateCompany.as_view(), name="create"),
    url(r'^update/(?P<pk>\d+)/$',views.UpdateCompany.as_view(),name='update'),
    url(r"^(?P<pk>[-\w]+)/$",views.SingleCompany.as_view(),name="single"),

]

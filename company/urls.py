from django.conf.urls import url
from company import views

app_name = 'company'

urlpatterns = [
    url(r'^$',views.CompanyListView.as_view(),name='list'),
    url(r'^(?P<pk>\d+)/$',views.CompanyDetailView.as_view(),name='detail'),
    url(r'^create/$',views.CompanyCreateView.as_view(),name='create'),
    url(r'^update/(?P<pk>\d+)/$',views.CompanyUpdateView.as_view(),name='update'),
    url(r'^delete/(?P<pk>\d+)/$',views.ComapnyDeleteView.as_view(),name='delete')
]

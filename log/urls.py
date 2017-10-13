from django.conf.urls import url

from . import views

app_name = 'log'

urlpatterns = [
    url(r'^$', views.LogListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', views.LogDetailView.as_view(), name='detail'),
    url(r'^create/$', views.LogCreateView.as_view(), name='create'),
    url(r'^update/(?P<pk>\d+)/$', views.LogUpdateView.as_view(), name='update'),
    url(r'^delete/(?P<pk>\d+)/$', views.LogDeleteView.as_view(), name='delete'),
]

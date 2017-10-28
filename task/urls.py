from django.conf.urls import url
from task import views

app_name = 'task'

urlpatterns = [
    url(r'^$',views.TaskListView.as_view(),name='list'),
    url(r'^(?P<pk>\d+)/$',views.TaskDetailView.as_view(),name='detail'),
    url(r'^create/(?P<pk>\d+)/$',views.TaskCreateView.as_view(),name='create'),
    url(r'^update/(?P<pk>\d+)/$',views.TaskUpdateView.as_view(),name='update'),
    url(r'^delete/(?P<pk>\d+)/$',views.TaskDeleteView.as_view(),name='delete'),
    url(r'^setting/create/(?P<pk>\d+)/$',views.TaskPropertyCreateView.as_view(),name='procreate'),
    url(r'^setting/update/(?P<pk>\d+)/$',views.TaskPropertyUpdateView.as_view(),name='proupdate'),
    url(r'^setting/delete/(?P<pk>\d+)/$',views.TaskPropertyDeleteView.as_view(),name='prodelete')

]

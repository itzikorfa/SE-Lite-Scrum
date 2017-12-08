from django.conf.urls import url
from task import views

app_name = 'task'

urlpatterns = [
    url(r'^$',views.TaskListView.as_view(),name='list'),
    url(r'^unassigned/(?P<sprint>\d+)/(?P<pk>\d+)/$',views.UnAssignListView.as_view(),name='unassignedlist'),
    url(r'^(?P<pk>\d+)/$', views.TaskDetailView.as_view(), name='detail'),
    url(r'^create/(?P<pk>\d+)/$',views.TaskCreateView.as_view(),name='create'),
    url(r'^update/(?P<pk>\d+)/$',views.TaskUpdateView.as_view(),name='update'),
    url(r'^finished/(?P<pk>\d+)/$',views.TaskFinished.as_view(),name='finished'),
    url(r'^delete/(?P<pk>\d+)/$',views.TaskDeleteView.as_view(),name='delete'),
    url(r'^setting/create/(?P<pk>\d+)/$',views.TaskPropertyCreateView.as_view(),name='procreate'),
    url(r'^setting/create/(?P<sprint>\d+)/(?P<pk>\d+)/$',views.TaskAssignViewView.as_view(),name='proassign'),
    url(r'^setting/update/(?P<pk>\d+)/$',views.TaskPropertyUpdateView.as_view(),name='proupdate'),
    url(r'^setting/delete/(?P<pk>\d+)/$',views.TaskPropertyDeleteView.as_view(),name='prodelete'),
    url(r'stage/(?P<pk>[-\w]+)/$', views.TaskPropertyChangeStageView.as_view(), name='stage_change'),

]

from django.conf.urls import url
from project import views

app_name = 'project'

urlpatterns = [
    url(r'^$',views.ProjectListView.as_view(),name='list'),
    url(r'^(?P<pk>\d+)/$',views.ProjectDetailView.as_view(),name='detail'),
    url(r'^create/$',views.ProjectCreateView.as_view(),name='create'),
    url(r'^update/(?P<pk>\d+)/$',views.ProjectUpdateView.as_view(),name='update'),
    url(r'^delete/(?P<pk>\d+)/$',views.ProjectDeleteView.as_view(),name='delete')
]

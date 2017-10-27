from django.conf.urls import url
from project import views

app_name = 'project'

urlpatterns = [
    url(r'^$',views.ProjectListView.as_view(),name='list'),
    url(r'^(?P<pk>\d+)/$',views.ProjectDetailView.as_view(),name='detail'),
    url(r'^create/(?P<pk>\d+)/$',views.ProjectCreateView.as_view(),name='create'),
    url(r'^update/(?P<pk>\d+)/$',views.ProjectUpdateView.as_view(),name='update'),
    url(r'^delete/(?P<pk>\d+)/$',views.ProjectDeleteView.as_view(),name='delete'),
    url(r'^backlog/create/(?P<pk>\d+)/$', views.ProjectBacklogCreateView.as_view(), name='blcreate'),
    url(r'^backlog/(?P<pk>\d+)/$',views.ProjectBacklogDetailView.as_view(),name='bldetail'),
    url(r'^backlog/update/(?P<pk>\d+)/$',views.ProjectBacklogUpdateView.as_view(),name='blupdate'),
    url(r'^setting/create/$', views.ProjectBacklogSettingCreateView.as_view(), name='createsetting'),
    url(r'^setting/(?P<pk>\d+)/$',views.ProjectBacklogSettingDetailView.as_view(),name='detailsetting'),
    url(r'^setting/update/(?P<pk>\d+)/$',views.ProjectBacklogSettingUpdateView.as_view(),name='updatesetting'),
]

from django.conf.urls import url
from sprint import views

app_name = 'sprint'

urlpatterns = [
    url(r'^$',views.SprintListView.as_view(),name='list'),
    url(r'^sprints/(?P<pk>\d+)/$',views.SprintListForProject.as_view(),name='prjlist'),
    url(r'^(?P<pk>\d+)/$',views.SprintDetailView.as_view(),name='detail'),
    url(r'^create/$',views.SprintCreateView.as_view(),name='create'),
    url(r'^update/(?P<pk>\d+)/$',views.SprintUpdateView.as_view(),name='update'),
    url(r'^delete/(?P<pk>\d+)/$',views.SprintDeleteView.as_view(),name='delete')
]

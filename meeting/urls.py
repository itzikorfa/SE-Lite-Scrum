from django.conf.urls import url
from meeting import views

app_name = 'meeting'

urlpatterns = [
    url(r'^$',views.MeetingListView.as_view(),name='list'),
    url(r'^(?P<pk>\d+)/$',views.MeetingDetailView.as_view(),name='detail'),
    url(r'^create/$',views.MeetingCreateView.as_view(),name='create'),
    url(r'^create/daily/(?P<slug>[-\w]+)/$',views.MeetingCreateDailyView.as_view(),name='createDaily'),
    url(r'^update/(?P<pk>\d+)/$',views.MeetingUpdateView.as_view(),name='update'),
    url(r'^delete/(?P<pk>\d+)/$',views.MeetingDeleteView.as_view(),name='delete')
]

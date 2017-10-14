from django.conf.urls import url
from todo import views

app_name = 'project'

urlpatterns = [
    url(r'^$',views.TodoListView.as_view(),name='list'),
    url(r'^(?P<pk>\d+)/$',views.TodoDetailView.as_view(),name='detail'),
    url(r'^create/$',views.TodoCreateView.as_view(),name='create'),
    url(r'^update/(?P<pk>\d+)/$',views.TodoUpdateView.as_view(),name='update'),
    url(r'^delete/(?P<pk>\d+)/$',views.TodoDeleteView.as_view(),name='delete'),
    
]

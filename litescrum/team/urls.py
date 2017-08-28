from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from .views import (
    team_create, team_detail, team_list, team_update, team_delete
)

urlpatterns = [
    url(r'^(?P<id>\d+)/$', team_detail, name='team_detail'),
    url(r'^create/$', team_create, name='team_create'),
    url(r'^$', team_list, name='team_list'),
    url(r'^(?P<id>\d+)/edit/$', team_update, name='team_update'),
    url(r'^(?P<id>\d+)/delete/$', team_delete, name='team_delete'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

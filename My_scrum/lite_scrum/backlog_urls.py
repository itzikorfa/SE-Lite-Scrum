from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from .views import (
    backlog_create, backlog_detail, backlog_list, backlog_update, backlog_delete
)

urlpatterns = [
    url(r'^(?P<id>\d+)/$', backlog_detail, name='backlog_detail'),
    url(r'^create/$', backlog_create, name='backlog_create'),
    url(r'^$', backlog_list, name='backlog_list'),
    url(r'^(?P<id>\d+)/edit/$', backlog_update, name='backlog_update'),
    url(r'^(?P<id>\d+)/delete/$', backlog_delete, name='backlog_delete'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

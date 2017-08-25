from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from .views import (
    product_backlog_create, product_backlog_detail, product_backlog_list, product_backlog_update, product_backlog_delete
)

urlpatterns = [
    url(r'^(?P<id>\d+)/$', product_backlog_detail, name='product_backlog_detail'),
    url(r'^create/$', product_backlog_create, name='product_backlog_create'),
    url(r'^$', product_backlog_list, name='product_backlog_list'),
    url(r'^(?P<id>\d+)/edit/$', product_backlog_update, name='product_backlog_update'),
    url(r'^(?P<id>\d+)/delete/$', product_backlog_delete, name='product_backlog_delete'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

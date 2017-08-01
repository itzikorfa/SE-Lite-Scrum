from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from .views import (
    product_create, product_detail, product_list, product_update, product_delete
)

urlpatterns = [
    url(r'^(?P<id>\d+)/$', product_detail, name='product_detail'),
    url(r'^create/$', product_create, name='product_create'),
    url(r'^$', product_list, name='product_list'),
    url(r'^(?P<id>\d+)/edit/$', product_update, name='product_update'),
    url(r'^(?P<id>\d+)/delete/$', product_delete, name='product_delete'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

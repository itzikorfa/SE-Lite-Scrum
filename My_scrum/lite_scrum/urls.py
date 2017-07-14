from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from .views import (
    company_create,
    company_delete, company_detail, company_list, company_update
)

urlpatterns = [
    url(r'^(?P<id>\d+)/$', company_detail, name='company_detail'),
    url(r'^create/$', company_create, name='company_create'),
    url(r'^$', company_list, name='company_list'),
    url(r'^(?P<id>\d+)/edit/$', company_update, name='company_update'),
    url(r'^(?P<id>\d+)/delete/$', company_delete, name='company_delete'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

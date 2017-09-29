
from django.conf.urls import url,include
from django.contrib.auth import views as auth_view
from . import views
app_name = 'member'

urlpatterns = [
    url(r'login/$', auth_view.LoginView.as_view(template_name="member/login.html"), name='login'),
    url(r'logout/$', auth_view.LogoutView.as_view(), name='logout'),
    url(r'sigup/$', views.SignUp.as_view(), name='signup'),
]

from django.conf.urls import url
from django.contrib.auth.views import LogoutView, LoginView

from users import views
from users.views import home

urlpatterns = [
    url(r'home$', home, name='user_home'),
    url(r'login/$', LoginView.as_view(template_name='users/login.html'), name='user_login'),
    url(r'logout/$', LogoutView.as_view(), name='user_logout'),
    url(r'signup/$', views.SignUp.as_view(), name='signup')
    ]
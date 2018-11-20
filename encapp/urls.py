from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView

from enc.views import home

urlpatterns = [
    url(r'login$', LoginView.as_view(template_name='users/login.html'), name='user_login'),
    url(r'logout$', LogoutView.as_view(), name='user_logout'),
]
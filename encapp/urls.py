from django.conf.urls import url

from encapp import views

urlpatterns = [
    url(r'^$', views.search_form, name='search'),
    url(r'^search/', views.search, name='search'),
    url(r'^suggest/$', views.suggest, name='suggest'),
]

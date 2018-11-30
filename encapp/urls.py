from django.conf.urls import url

from encapp import views

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^search/', views.search, name='search'),
    url(r'^favorite/', views.FavoritesCreateView.as_view(), name='favorite'),
    url(r'^favorites/', views.FavoritesDetailView.as_view(), name='favorites'),
]

from django.urls import path
from . import views


urlpatterns = [
	path('', views.home, name='home'),
	path('aboutUs/', views.aboutUs, name='aboutUs'),
	path('posts/', views.posts, name='posts'),
	path('team/', views.team, name='team'),
	path('contact/', views.contact, name='contact'),
]

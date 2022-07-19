from django.urls import path
from . import views


urlpatterns = [
	path('', views.home, name='home'),
	path('about/', views.about, name='about'),
	path('posts/', views.posts, name='posts'),
	path('authors/', views.authors, name='authors'),
	path('contact/', views.contact, name='contact'),
        path('background/', views.background, name='background'),
        path('alu/', views.alu, name='alu'),
        path('mauritius/', views.mauritius, name='mauritius'),
        path('social/', views.social, name='social'),
        path('career/', views.career, name='career'),
        path('pictures/', views.pictures, name='pictures'),
        path('comments/', views.comments, name='comments')	
]

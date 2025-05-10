from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('create/', views.create_post, name='create_post'),
    path('register/', views.register, name='register'),
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('like/<int:post_id>/', views.like_image, name='like_image'),
    path('profile/', views.profile, name='profile'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
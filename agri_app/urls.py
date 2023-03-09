from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index, name="home"),
    path('about/', views.about, name="about"),
    path('signup/', views.signup, name="signup"),
    path('profile/', views.profile, name="profile"),
    path('blogs/', views.blogs, name="blogs"),
    path('login/', auth_views.LoginView.as_view(template_name = 'login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'logout.html'), name = 'logout'),
    # path('login/', views.login, name="login"),
    # path("room/", views.room, name="room"),
]

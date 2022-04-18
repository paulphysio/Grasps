from re import template
from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('home/', views.home, name="home"),
    path('', views.home, name="home"),
    path('profile/', views.profile, name="profile"),
    path('signup/', views.signup, name="signup"),
    path('login/', auth_view.LoginView.as_view(template_name = 'Grasps/Login.html'), name = "login"),
    path('logout/', auth_view.LogoutView.as_view(template_name = 'Grasps/Logout.html'), name = "logout"),
    

]
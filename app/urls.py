
from django.contrib import admin
from django.urls import path,include
from app import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.Home, name="index"),
    path('resume', views.Resume, name="resume"),
    path('game', views.Project1, name="game"),
    path('django-site', views.Project2, name="site"),
    path('signup', views.Signup, name="Signup"),
    path('login', views.loginUser, name="loginUser"),
    path('soon', views.build, name="build"),
    path('logout', views.logoutUser, name="logoutUser"),
    path('feedback', views.Feedback, name="Feedback"),
    path('reset', auth_views.PasswordResetView.as_view(template_name="reset.html"), name="reset_password"),
    path('reset_done', auth_views.PasswordResetDoneView.as_view(template_name="reset_sent.html"),name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"),name="password_reset_confirm"),
    path('reset_complete', auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"), name="password_reset_complete"),
]
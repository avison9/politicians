from django.urls import path
from . import views


urlpatterns = [

    path('', views.home, name='home'),

    path('register', views.register, name='register'),

    path('update', views.edit_form, name='user_update'),

    path('login', views.login, name='login'),

    path('logout', views.logout, name='logout'),

    path('dashboard', views.dashboard, name='dashboard'),


]
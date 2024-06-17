from django.urls import path
from . import views


urlpatterns = [

    path('', views.home, name='home'),

    path('register', views.register, name='register'),

    path('update', views.edit_form, name='userupdate'),

    path('login', views.login, name='login')


]
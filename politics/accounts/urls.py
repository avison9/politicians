from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [

    path('', views.home, name='home'),

    path('register', views.register, name='register'),

    path('update', views.edit_form, name='user_update'),

    path('login', views.login, name='login'),

    path('logout', views.logout, name='logout'),

    path('dashboard', views.dashboard, name='dashboard'),

    # path('password_reset', auth_views.password_reset, name='password_reset'),

    # path('password_reset_done', auth_views.password_reset_done, name='password_reset_done'),

    # path('reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #     auth_views.password_reset_confirm, name='password_reset_confirm'),

    # path('reset_done', auth_views.password_reset_complete, name='password_reset_complete'),


]
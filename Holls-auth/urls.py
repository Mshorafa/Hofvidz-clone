from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


app_name = 'Holls-auth'

urlpatterns = [
    path('',views.index ,name='index'),
    path('signup/',views.SignUp.as_view(),name='SignUp'),
    path('login/',auth_views.LoginView.as_view(),name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='LogoutView'),
    path('dashbord/',views.dashbord,name = 'dashbord')
]
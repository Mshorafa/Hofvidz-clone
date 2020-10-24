from django.urls import path
from . import views

app_name = 'Holls'

urlpatterns = [
    path('',views.index ,name='index')
]
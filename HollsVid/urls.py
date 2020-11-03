from django.urls import path
from . import views


app_name = 'HollsVid'

urlpatterns = [
    path('create/', views.CreateHolls.as_view(),name='createHolls'),
    path('<int:pk>/detials', views.detailHoll.as_view(),name='detailHoll'),
    path('<int:pk>/update', views.UpdatelHoll.as_view(),name='UpdatelHoll'),
    path('<int:pk>/delete', views.DeleteHolls.as_view(),name='DeleteHolls'),
    path('<int:pk>/add', views.AddVideos,name='add-videos'),
    path('search/videos', views.search_videos,name='search_videos'),
]
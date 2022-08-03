from django.urls import path, include
#from watchlist_app.api.views import movie_list, movie_detail
from watchlist_app.api.views import WatchListAV, WatchDetailAV , homepage_, StreamListAV, StreamDetailsAV

urlpatterns = [
    path('',homepage_, name='homepage'),
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>', WatchDetailAV.as_view(), name = 'movie-detail'),
    path('stream/',StreamListAV.as_view(), name= 'stream-list'),
    path('stream/<int:pk>', StreamDetailsAV.as_view(), name='stream-detail')
    
    ]

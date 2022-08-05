from django.urls import path, include
#from watchlist_app.api.views import movie_list, movie_detail
from watchlist_app.api.views import WatchListAV, WatchDetailAV , homepage_, StreamListAV, StreamDetailsAV, ReviewList, ReviewDetail

urlpatterns = [
    path('',homepage_, name='homepage'),
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>', WatchDetailAV.as_view(), name = 'movie-detail'),
    path('stream/',StreamListAV.as_view(), name= 'stream-list'),
    path('stream/<int:pk>', StreamDetailsAV.as_view(), name='stream-detail'),
    path('review',ReviewList.as_view(), name='review-list'),
    path('review/<int:pk>',ReviewDetail.as_view(), name='review-detail')
    
    
    ]

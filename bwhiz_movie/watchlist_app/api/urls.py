from django.urls import path, include
from rest_framework.routers import DefaultRouter
#from watchlist_app.api.views import movie_list, movie_detail
from watchlist_app.api.views import (WatchListAV, WatchDetailAV , homepage_, 
                                     StreamListAV, StreamDetailsAV, ReviewList, 
                                     ReviewDetail,ReviewCreate, StreamPlatformVS)

router = DefaultRouter()
router.register('stream', StreamPlatformVS, basename = 'streamplatform' )


urlpatterns = [
    
    path('',homepage_, name='homepage'),
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>/', WatchDetailAV.as_view(), name = 'movie-detail'),
    
    path('', include(router.urls)),
    # path('stream/',StreamListAV.as_view(), name= 'stream-list'),
    # path('stream/<int:pk>', StreamDetailsAV.as_view(), name='stream-detail'),
    path('<int:pk>/review-create',ReviewCreate.as_view(), name='review-create'),
    path('<int:pk>/reviews',ReviewList.as_view(), name='review-list'),
    path('review/<int:pk>',ReviewDetail.as_view(), name='review-detail')
    
    
    ]

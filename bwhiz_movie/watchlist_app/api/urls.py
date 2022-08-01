from django.urls import path, include
#from watchlist_app.api.views import movie_list, movie_detail
from watchlist_app.api.views import MovieListAV, MovieDetailAV , homepage_

urlpatterns = [
    path('',homepage_, name='homepage'),
    path('list/', MovieListAV.as_view(), name='movie-list'),
    path('<int:pk>', MovieDetailAV.as_view(), name = 'movie-detail'),
    
    ]

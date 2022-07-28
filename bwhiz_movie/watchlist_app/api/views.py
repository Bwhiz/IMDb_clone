from rest_framework.response import Response
from watchlist_app.models import Movie
from watchlist_app.api.serializers import MovieSerializer


def movie_list(request):
    movie = Movie.objects.all()
    serializer = MovieSerializer(movie)
    
    return Response(serializer.data)


def movie_detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    serializer = MovieSerializer(movie)
    
    return Response(serializer.data)
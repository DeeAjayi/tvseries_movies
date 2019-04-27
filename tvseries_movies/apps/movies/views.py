from rest_framework import generics
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer, BrowsableAPIRenderer
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Movie
from .models import URL
from .serializers import MovieSerializer
from .serializers import URLSerializer


class MovieListView(generics.ListCreateAPIView):
    renderer_classes = [BrowsableAPIRenderer, TemplateHTMLRenderer]
    template_name = 'movies_app/movies_list.html'
    # queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    name = 'movie-list'

    filter_fields = (
        'title',
        'release_year'
    )

    search_fields = (
        '^title'
    )

    def get(self, request):
        queryset = Movie.objects.all()[:5]
        return Response({'movies': queryset})


class MovieDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    name = 'movie-detail'


class URLListView(generics.ListCreateAPIView):
    queryset = URL.objects.all()
    serializer_class = URLSerializer
    name = 'url-list'


class URLDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = URL.objects.all()
    serializer_class = URLSerializer
    name = 'url-detail'


from rest_framework import serializers
from django_filters import AllValuesFilter, DateTimeFilter, NumberFilter
from django_filters import rest_framework as filters
from .models import Movie, URL


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    download_urls = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='url-detail')

    class Meta:
        model = Movie
        fields = (
            'pk',
            'title',
            'release_year',
            'image_url',
            'trailer_url',
            'imdb_rating',
            'download_urls'
        )

    def __str__(self):
        return self.title


class URLSerializer(serializers.HyperlinkedModelSerializer):
    movie = serializers.SlugRelatedField(queryset=Movie.objects.all(), slug_field='slug')
    filter_fields = (
        'name',
        'movie'
    )

    class Meta:
        model = URL
        fields = (
            'name',
            'movie',
            'url'
        )

    def __str__(self):
        return self.movie + ' - ' + self.name
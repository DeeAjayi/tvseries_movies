import json
from django.utils.text import slugify
from tvseries_movies.apps.movies.models import Movie, URL

# To add data to the json file
with open('sample.json', 'r') as read_file:
        datastore = json.load(read_file)


for movie in datastore:
    movie_model = Movie.objects.create(
        title=datastore[str(movie)]['title'],
        release_year=datastore[str(movie)]['year'],
        image_url=datastore[str(movie)]['image_url'],
        trailer_url=datastore[str(movie)]['trailer_url'],
        imdb_rating=datastore[str(movie)]['rating'],
        slug=slugify(datastore[str(movie)]['title']))

    for url in datastore[str(movie)]["download_urls_info"]:
        url_model = URL.objects.create(
            movie=movie_model,
            name=url,
            url=datastore[str(movie)]["download_urls_info"][str(url)]
        )

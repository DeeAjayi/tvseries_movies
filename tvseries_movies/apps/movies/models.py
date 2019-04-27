from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_year = models.IntegerField()
    slug = models.SlugField(unique=True)
    image_url = models.URLField()
    trailer_url = models.URLField()
    imdb_rating = models.FloatField()

    class Meta:
        ordering = ['-release_year', '-pk', 'title']
        get_latest_by = ['id']

    def __str__(self):
        return self.title

    def get_title(self):
        return self.title

    def get_urls(self):
        return self.download_urls


class URL(models.Model):
    name = models.CharField(max_length=30)
    movie = models.ForeignKey(Movie, related_name='download_urls', on_delete=models.CASCADE)
    url = models.URLField()

    def __str__(self):
        return str(self.movie) + ' - ' + self.name

    def get_url(self):
        return self.url

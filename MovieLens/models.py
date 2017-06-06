from django.db import models


# Create your models here.
class MovieLensMovie(models.Model):
    movieId = models.CharField(max_length=10)
    title = models.CharField(max_length=256)
    genres = models.CharField(max_length=256)

    def __str__(self):
        return self.title

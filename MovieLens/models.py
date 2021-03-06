from django.db import models


# Create your models here.
class MovieLensMovie(models.Model):
    movieId = models.CharField(max_length=10)
    title = models.CharField(max_length=256)
    genres = models.CharField(max_length=256)

    def __str__(self):
        return self.title

    def GetTitle(self):
        return self.title

    def GetMovieId(self):
        return self.movieId

    def GetGenres(self):
        return self.genres

    def GetAllMovieInfo(self):
        redict = {
            'title': self.title,
            'movieId': self.movieId,
            'genres': self.genres
            }
        return redict

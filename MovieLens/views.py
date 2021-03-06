import json
import requests
import random

from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from .models import MovieLensMovie


# Create your views here.
@login_required
def MovieLens(request):
    # who u are
    if request.method == 'POST':
        return redirect('MovieLensUser', request.POST['quantity'])
    # what movie u want to check
    context = {'movie': []}
    IDList = random.sample(range(1, 27278), 10)
    for ID in IDList:
        movieObject = MovieLensMovie.objects.get(pk=ID)
        movie = {
            'title': movieObject.GetTitle(),
            'movieId': movieObject.GetMovieId(),
            'genres': movieObject.GetGenres()
            }
        context['movie'].append(movie)
    return render(request, 'MovieLens/index.html', context)


@login_required
def MovieLensAUser(request, userID=None):
    if userID is not None:
        context = {
            'movie': [],
            'USER': userID,
            }
        if request.user.get_short_name() is not None:
            context['username'] = request.user.get_short_name()
        else:
            context['username'] = request.user.get_username()
        url = "http://140.113.207.198:3000/action"
        urlwithID = "{0}?userID={1}".format(url, userID)
        reURL = requests.get(urlwithID)
        if reURL.status_code == 200:
            movieJson = json.loads(reURL.text)
            context['JSON'] = movieJson
            if 'error' in movieJson:
                context['error'] = movieJson['error']
            for val in movieJson:
                movie = MovieLensMovie.objects.get(movieId=val['movieID'])
                moviedic = {
                    'title': movie.GetTitle(),
                    'movieId': movie.GetMovieId(),
                    'genres': movie.GetGenres()
                    }
                context['movie'].append(moviedic)
            return render(request, 'MovieLens/user.html', context)
        else:
            context = {
                'movie': [],
                'ERROR': "Get requests fail status_code:{}".format(
                    reURL.status_code),
                }
    else:
        return redirect('MovieLens')


@login_required
def MovieLensAMovie(request, movieID=None):
        if movieID is not None:
            movie = MovieLensMovie.objects.get(movieId=movieID)
            context = {
                'movie': [],
                'thismovie': movie.GetAllMovieInfo(),
                }
            if request.user.get_short_name() is not None:
                context['username'] = request.user.get_short_name()
            else:
                context['username'] = request.user.get_username()
            url = "http://140.113.207.198:3000/action"
            urlwithID = "{0}?movieID={1}".format(url, movieID)
            reURL = requests.get(urlwithID)
            if reURL.status_code == 200:
                movieJson = json.loads(reURL.text)
                context['JSON'] = movieJson
                if 'error' in movieJson:
                    context['error'] = movieJson['error']
                for val in movieJson[1:]:
                    movie = MovieLensMovie.objects.get(movieId=val['movieID'])
                    moviedic = {
                        'title': movie.GetTitle(),
                        'movieId': movie.GetMovieId(),
                        'genres': movie.GetGenres()
                        }
                    context['movie'].append(moviedic)
                return render(request, 'MovieLens/movie.html', context)
            else:
                context = {
                    'movie': [],
                    'ERROR': "Get requests fail status_code:{}".format(
                        reURL.status_code),
                    }
        else:
            return redirect('MovieLens')

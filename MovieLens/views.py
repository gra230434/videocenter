import json
import requests
import random

from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def MovieLens(request):
    # who u are
    # what movie u want to check
    context = {}
    movieID = random.sample(range(1, 131262), 10)
    context['movie'] = movieID
    return render(request, 'MovieLens/index.html', context)


@login_required
def MovieLensUser(request, userID=None):
    if userID is not None:
        url = "http://140.113.207.198:3000/action"
        urlwithID = "{0}?userID={1}".format(url, userID)
        reURL = requests.get(urlwithID)
        if reURL.status_code == 200:
            movieJson = json.loads(reURL.text)
            movieList = []
            for val in movieJson:
                movieList.append(val['movieID'])
            context = {'movie': movieList}
            return render(request, 'MovieLens/user.html', context)
    else:
        if request.method == 'POST':
            if request.POST['userID'] is not None:
                userID = request.POST['userID']
                return redirect('MovieLensUser', userID)
        return redirect('MovieLens')


@login_required
def MovieLensMovie(request, movieID=None):
        if movieID is not None:
            url = "http://140.113.207.198:3000/action"
            urlwithID = "{0}?movieID={1}".format(url, movieID)
            reURL = requests.get(urlwithID)
            if reURL.status_code == 200:
                movieJson = json.loads(reURL.text)
                movieList = []
                for val in movieJson:
                    movieList.append(val['movieID'])
                context = {'movie': movieList}
                return render(request, 'MovieLens/user.html', context)
            pass
        else:
            if request.method == 'POST':
                if request.POST['userID'] is not None:
                    userID = request.POST['userID']
                    return redirect('MovieLensUser', userID)

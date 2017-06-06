from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.MovieLens, name='MovieLens'),
    url(
        r'^user/(?P<userID>[0-9]{6})/$',
        views.MovieLensAUser, name='MovieLensUser'
        ),
    url(
        r'^movie/(?P<movieID>[0-9]{6})/$',
        views.MovieLensAMovie, name='MovieLensMovie'),
    ]

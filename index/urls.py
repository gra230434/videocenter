from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(
        r'^SingIn/$',
        auth_views.LoginView.as_view(template_name='index/login.html'),
        name='SingIn'
        ),
    url(
        r'^SingOut/$',
        auth_views.LogoutView.as_view(template_name='index/logout.html'),
        name='SingOut'),
    url(
        r'^SingUp/$',
        views.register_page,
        name='SingUp'
        ),
    ]

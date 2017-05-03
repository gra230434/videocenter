from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(
        r'^SingIn/$',
        auth_views.LoginView.as_view(template_name='index/login.html'),
        name='login'
        ),
    url(r'^SingOut/$', views.logout_action, name='logout'),
    url(r'^SingUp/$', views.register_page, name='SingUp'),
    # Restful API
    url(r'^post/register/', views.register_action, name='register')
    ]

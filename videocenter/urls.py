from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login_page, name='login'),
    url(r'^logout/$', views.logout_action, name='logout'),
    url(r'^post/video/login_action/', views.login_action, name='loginaction')
]

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='account_index'),
    url(r'^edit/$', views.index, name='account_edit'),
    ]

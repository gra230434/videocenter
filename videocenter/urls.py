from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='vcenter_index'),
    url(r'^animate/$', views.animate, name='vcenter_animate')
    ]

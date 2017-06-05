from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='vcenter_index'),
    url(r'^animate/$', views.animate, name='vcenter_ani'),
    url(r'^animate/(?P<aniID>[0-9]{4})/$',
        views.anidetail, name='vcenter_anidetail'),
    url(r'^edit/animate/$',
        views.editanicreate, name='VC_edit_ani'),
    url(r'^edit/animate/(?P<aniID>[0-9]{4})/$',
        views.editanidetail.as_view(), name='VC_edit_anidetail'),
    url(r'^edit/animate/(?P<aniID>[0-9]{4})/(?P<is_fail>[0-9]{1})$',
        views.editanidetail.as_view(), name='VC_edit_anidetail'),
    ]

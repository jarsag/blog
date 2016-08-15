from django.conf.urls import url
from django.contrib import admin
from .views import(
    post_list,
    post_create,
    post_detail,
    post_updated,
    post_delete,
    comm_create,
    comm_detail,
    comm_delete,
)

urlpatterns = [
	url(r'^$', post_list, name='list'),
    url(r'^create/$', post_create),
    url(r'^(?P<id>\d+)/$', post_detail, name='detail'),
    url(r'^(?P<id>\d+)/edit/$', post_updated, name='update'),
	url(r'^(?P<id>\d+)/delete/$', post_delete),
    url(r'^(?P<id>\d+)/comment/$', comm_create),
    url(r'^(?P<id>\d+)/$', comm_detail, name='detail'),
    url(r'^(?P<id>\d+)/comment/(?P<pk>\d+)/delete/$', comm_delete),
#	url(r'^posts/$', "<appname>.views.<function>")

]
 

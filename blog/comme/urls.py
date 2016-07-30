from django.conf.urls import url
from django.contrib import admin
from .views import comm_create, comm_detail



urlpatterns = [
	# url(r'^$', post_list, name='list'),
    url(r'^create/$', comm_create),
    url(r'^(?P<id>\d+)/$', comm_detail, name='detail'),
]

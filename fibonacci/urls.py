from django.contrib import admin
from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^number/(?P<number>\d+)/$', views.get_number, name='get_number')
]
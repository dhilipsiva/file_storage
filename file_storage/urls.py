from django.conf.urls import patterns, url
from file_storage.views import index

urlpatterns = patterns(
    '',
    url(r'^(?P<path>.*)$', index),
)

from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^vote$', 'gleeoke.views.vote'),
    (r'^$', 'gleeoke.views.choose'),
)
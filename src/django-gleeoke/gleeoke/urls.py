from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^vote$', 'gleeoke.views.vote'),
    (r'^rankings$', 'gleeoke.views.rankings'),
    (r'^$', 'gleeoke.views.choose'),
)
from django.conf.urls.defaults import *

urlpatterns = patterns('walkathon.views',
        (r'^$', 'home'),
        (r'^participant/(\d+)/$', 'participant_detail'),
        (r'^sponsor/(\d+)/$', 'sponsor_detail'),
)

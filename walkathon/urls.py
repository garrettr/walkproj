from django.conf.urls.defaults import *

urlpatterns = patterns('walkathon.views',
        (r'^$', 'home'),
        (r'^p/(\d+)/$', 'participant_detail'),
        (r'^s/(\d+)/$', 'sponsor_detail'),
        (r'^register/$', 'register_participant'),
        (r'^register/thanks/(\d+)/$', 'register_thanks'),
        (r'^sponsor/$', 'register_sponsor'),
        (r'^sponsor/thanks/(\d+)/$', 'sponsor_thanks'),
)

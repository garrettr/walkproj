# walkathon admin.py

from django.contrib import admin
from walkathon.models import Participant, Sponsor

admin.site.register(Participant)
admin.site.register(Sponsor)

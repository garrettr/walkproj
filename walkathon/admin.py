# walkathon admin.py

from django.contrib import admin
from walkathon.models import Participant, Sponsor

class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'created_on')

class SponsorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'created_on')

admin.site.register(Participant, ParticipantAdmin)
admin.site.register(Sponsor, SponsorAdmin)

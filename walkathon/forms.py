#from django import forms
from walkathon.models import Participant, Sponsor
from django.forms import ModelForm

class ParticipantForm(ModelForm):
    '''
    Auto generated form to create Participants
    '''
    class Meta:
        model = Participant
        exclude = ('active', 'created_on')

class SponsorForm(ModelForm):
    '''
    Auto generated form to create Sponsors
    '''
    class Meta:
        model = Sponsor
        exclude = ('active', 'created_on')

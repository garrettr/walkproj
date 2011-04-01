# Create your views here.
from django.shortcuts import render_to_response
from walkathon.models import Participant, Sponsor

def home(request):
    '''
    Display top 10 participants, and just registered or something.
    Have links for donating and registering to walk.
    '''
    recent_participants = Participant.objects.all().order_by('created_on')[:5]
    return render_to_response('walkathon/home.html', 
            {'recent_participants': recent_participants})

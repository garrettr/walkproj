# Create your views here.
from django.shortcuts import render_to_response
from walkathon.models import Participant, Sponsor

def home(request):
    '''
    Display top 10 participants, and just registered or something.
    Have links for donating and registering to walk.
    '''
    recent_participants = Participant.objects.all().order_by('-created_on')[:5]
    recent_sponsors = Sponsor.objects.all().order_by('-created_on')[:5]
    return render_to_response('walkathon/home.html', 
            {'recent_participants': recent_participants,
                'recent_sponsors': recent_sponsors})

def participant_detail(request, pid):
    '''
    Display a single participant's information.
    '''
    p = Participant.objects.get(id=pid)
    return render_to_response('walkathon/participant_detail.html',
            {'p': p})

def sponsor_detail(request, sid):
    '''
    Display a single sponsor's information.
    '''
    s = Sponsor.objects.get(id=sid)
    return render_to_response('walkathon/sponsor_detail.html',
            {'s': s})

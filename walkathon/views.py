# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from walkathon.models import Participant, Sponsor
from walkathon.forms import ParticipantForm, SponsorForm
from django.template import RequestContext

import datetime

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

def register_participant(request):
    '''
    Form for a visitor to sign up as a participant in the March
    '''
    if request.method == 'POST':
        form = ParticipantForm(request.POST)
        if form.is_valid():
            # Create a new Participant object
            # Now we need to set active and created_on
            p = form.save(commit=False)
            p.active = True
            p.created_on = datetime.datetime.now()      # timestamp
            p.save()
            return HttpResponseRedirect(reverse(
                'walkathon.views.register_thanks', args=(p.id,)
                ))
    else:
        form = ParticipantForm()

    variables = RequestContext(request, {
        'form': form
    })
    return render_to_response('walkathon/register_participant.html', variables)

def register_sponsor(request):
    '''
    Form for a visitor to sponsor someone in the March
    '''
    if request.method == 'POST':
        form = SponsorForm(request.POST)
        if form.is_valid():
            # Create a new Participant object
            # Now we need to set active and created_on
            s = form.save(commit=False)
            s.active = True
            s.created_on = datetime.datetime.now()      # timestamp
            s.save()
            return HttpResponseRedirect(reverse(
                'walkathon.views.sponsor_thanks', args=(s.id,)
                ))
    else:
        form = SponsorForm()

    variables = RequestContext(request, {
        'form': form
    })
    return render_to_response('walkathon/register_sponsor.html', variables)

def register_thanks(request, pid):
    '''
    Display a "Thank You" for a participant who has successfully registered
    '''
    p = Participant.objects.get(id=pid)
    return render_to_response('walkathon/register_thanks.html', {'p': p})

def sponsor_thanks(request, sid):
    '''
    Display a "Thank You" for a sponsorship
    '''
    s = Sponsor.objects.get(id=sid)
    return render_to_response('walkathon/sponsor_thanks.html', {'s': s})

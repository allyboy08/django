from django.shortcuts import render
# from django.http import HttpResponse
from .models import Meetup
# Create your views here.

def index(request):
    meetups = Meetup.objects.all()
    return render(request, 'meetups/index.html', {
        
        'meetups': meetups
    })
    
def meetup_details(request, meetup_slug):
    selected_meetup = Meetup.objects.get(slug)
    return render(request, 'meetups/meetup-details.html', {
        'meetup_title': selected_meetup['title'],
        'meetup_description': selected_meetup['description']
    })



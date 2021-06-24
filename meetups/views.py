from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.

def index(request):
    meetups = [
        {'title': 'A First Meetup', 'location': 'new york', 'slug': 'a-first-meetup'},
        {'title': 'A Second Meetup', 'location': 'france', 'slug': 'a-second-meetup'}
    ]
    return render(request, 'meetups/index.html', {
        'show_meetups': True,
        'meetups': meetups
    })



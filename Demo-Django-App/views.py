from django.shortcuts import render
from django.http import HttpResponse
from .models import Meetup

# Create your views here.
def index(request):
    meetups = Meetup.objects.all()
    return render(request, 'meetups/index.html', {
        'meetups': meetups
    })


def meetup_details(request, pk):
    try:
        selected_meetups = Meetup.objects.get(id=pk)

        return render(request, 'meetups/meetup-details.html', {
            'meetup_found': True,
            'meetup_title': selected_meetups.title,
            'meetup_description': selected_meetups.description
        })
    except Exception as exc:
        return render(request, 'meetups/meetup-details.html', {
            'meetup_found': False
        })
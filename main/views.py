from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import Event, User
from django.views import generic
# Create your views here.

def mainpage(request):
    events = Event.objects.all().count()
    users = User.objects.all().count()

    context = {
        'events' : events,
        'users' : users
    }

    return render(request, 'main.html', context = context)

class EventListView(generic.ListView):
    model = Event 
    context_object_name = 'eventlist'

class EventDetailView(generic.DetailView):
    model = Event

from .forms import EventForm, SignupForm

def createEvent(request):
    form = EventForm()
    if request.method == 'POST':
        print('Priting POST:', request.POST)
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print("form invalid")
        
    context = {'form': form}
    return render(request, 'createevent/create_event.html', context = context)

def updateEvent(request, pk):
    event = Event.objects.get(id = pk)
    form = EventForm()

    if request.method == 'POST':
        print('Priting POST:', request.POST)
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
        else:
            print("form invalid")        
    context = {'form': form}
    return render(request, 'createevent/create_event.html', context = context)
    
def deleteEvent(request, pk):
    event = Event.objects.get(id = pk)
    if request.method == "POST":
        event.delete()
    context = {'item': event}
    return render(request, 'createevent/delete_event.html', context = context)
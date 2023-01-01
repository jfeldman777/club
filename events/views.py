from django.shortcuts import render,redirect
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .models import Event,Venue

from .forms import VenueForm
from django.http import HttpResponseRedirect

def show_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    return render(request,'events/show_venue.html',
    {'venue':venue})

# Create your views here.def
def list_venues(request):
        venue_list = Venue.objects.all()
        return render(request, 'events/venue_list.html',
        {"venue_list":venue_list})

def search_venues(request):
    if request.method == "POST":
        searched = request.POST["searched"]

        venues = Venue.objects.filter(name__contains=searched)
        return render(request, 'events/search_venues.html',
        {
            "searched":searched,
            "venues":venues
        })
    else:
        return render(request, 'events/search_venues.html',{
            "searched":searched,
            "venues":venues
        })


def  update_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    form = VenueForm(request.POST or None, instance=venue)
    if form.is_valid():
        form.save()
        return redirect('list-venues')

    return render(request,"events/update_venue.html", {
'venue':venue,
'form':form
    })


def add_venue(request):
    submitted = False
    if request.method == "POST":
        form = VenueForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_venue?submitted=True')
    else:
        form = VenueForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'events/add_venue.html',
    {'form':form,
    'submitted':submitted,})


def all_events(request):
    event_list = Event.objects.all()
    return render(request, 'events/event_list.html',
    {"event_list":event_list})

def home(request,year=datetime.now().year,month=datetime.now().strftime('%B')):
    name = 'Joe'
    month = month.capitalize()
    month_number = list(calendar.month_name).index(month);
    month_number = int(month_number)
    #create calendar
    cal = HTMLCalendar().formatmonth(year, month_number)
    now = datetime.now()
    current_year = now.year
    time = now.strftime('%I:%M:%p') #:@S')
    #convert mon from str to num
    return render(request,'events/home.html',{
        "name": name,
        "year": year,
        "month": month,
        "month_number":month_number,
        "cal": cal,
        "current_year":current_year,
        "time":time,
    })

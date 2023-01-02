from django import forms
from django.forms import ModelForm
from .models import Venue, Event

class VenueForm(ModelForm):
    class Meta:
        model = Venue
        fields = "__all__"
        labels = {
'name':'',
'address':'',
'zip_code':'',
'phone':'',
'web':'',
'email_address':''
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control','placeholder':'name'}),
            'address':  forms.TextInput(attrs={'class':'form-control','placeholder':'address'}),
            'zip_code':  forms.TextInput(attrs={'class':'form-control','placeholder':'zip_code'}),
            'phone':  forms.TextInput(attrs={'class':'form-control','placeholder':'phone'}),
            'web':  forms.TextInput(attrs={'class':'form-control','placeholder':'web'}),
            'email_address': forms.TextInput(attrs={'class':'form-control','placeholder':'email'}),
        }

#name event_date venue manager description attendee
class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ('name','event_date','venue', 'manager', 'attendee', 'description')
        labels = {
'name':'',
'event_date':'YYYY-MM-DD HH:MM:SS',
'venue':'Venue',
'manager':'Manager',
'attendee':'Attendees',
'description':'',

        }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control','placeholder':'event name'}),
            'event_date':  forms.TextInput(attrs={'class':'form-control','placeholder':'event date'}),
            'venue':  forms.Select(attrs={'class':'form-select','placeholder':'venue'}),
            'manager':  forms.Select(attrs={'class':'form-selkect','placeholder':'manager'}),
            'attendee': forms.SelectMultiple(attrs={'class':'form-control','placeholder':'attendees'}),
            'description':  forms.Textarea(attrs={'class':'form-control','placeholder':'description'}),
        }

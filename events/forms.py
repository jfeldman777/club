from django import forms
from django.forms import ModelForm
from .models import Venue

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

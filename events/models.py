from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Venue(models.Model):
    name = models.CharField('Venue name',max_length=120)
    address = models.CharField(max_length=300)
    zip_code = models.CharField('Zip Code',max_length=15, blank=True,null=True,)
    phone = models.CharField('Contact Phone',max_length=9)
    web = models.URLField('Website Address',blank=True,null=True,)
    email_address = models.EmailField('Email Address',blank=True,null=True,)

    def __str__(self):
        return self.name

class MyClubUser(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email_address = models.EmailField('User Email')

    def __str__(self):
        return self.first_name + ' ' + self.last_name
#name event_date venue manager description attendee
class Event(models.Model):
    name = models.CharField('Event Name', max_length=120)
    event_date = models.DateTimeField('Event Date')
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    #venue = models.CharField(max_length=120)
    manager = models.ForeignKey(User,blank=True,null=True,on_delete=models.SET_NULL)
    description = models.TextField(blank=True)
    attendee = models.ManyToManyField(MyClubUser)

    def __str__(self):
        return self.name

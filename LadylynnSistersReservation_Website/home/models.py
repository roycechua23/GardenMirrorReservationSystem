from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone 

# Create your models here.
class UserProfileInfo(models.Model):
    
    user = models.OneToOneField(User)
    contact = models.CharField(max_length=15)
    # please pip install pillow before using 
    # Image field
    profile_pic = models.ImageField(blank=True,upload_to='profile_pics')
    
    def __str__(self):
        return self.user.username

class CateringPackages(models.Model):
    
    name = models.CharField(max_length=100,blank=False)
    capacity = models.PositiveIntegerField(default=50)
    description = models.CharField(max_length=256,blank=False, null=False)
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Foods(models.Model):
    # To be updated when crud operations on reservation are working
    food_name = models.CharField(max_length=100)
    food_package = models.ManyToManyField("CateringPackages")

class Reservation(models.Model):
    
    reserver = models.ForeignKey('UserProfileInfo', related_name='reservers', on_delete=models.CASCADE)
    package = models.ForeignKey('CateringPackages',related_name='packages',on_delete=models.CASCADE)
    event_type = models.CharField(max_length=100)
    currentdate = models.DateTimeField(auto_now=True)
    event_date = models.DateField()
    event_timestart = models.TimeField()
    event_timeend = models.TimeField()
    status = models.BooleanField(default=False)

    def completed(self):
        self.status = True
        self.save()

    def completed_eventslist(self):
        pass

    def __str__(self):
        eventname = "{} {} ({})".format(str(self.reserver.user.first_name),self.event_type,self.reserver)
        return eventname
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone 


from django.contrib.sessions.models import Session
# Create your models here.
class UserProfileInfo(models.Model):
    
    user = models.OneToOneField(User)
    contact = models.CharField(max_length=15)
    # please pip install pillow before using 
    # Image field
    profile_pic = models.ImageField(blank=True,upload_to='profile_pics')
    
    def __str__(self):
        return self.user.username

class EventArea(models.Model):

    name = models.CharField(max_length=100,unique=True)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class CateringPackage(models.Model):
    
    name = models.CharField(max_length=100,blank=False)
    pax = models.PositiveIntegerField(default=50,null=False)
    description = models.CharField(max_length=256,blank=False)
    # area  = models.ForeignKey('EventArea', related_name='area', on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    
    def __str__(self):
        return self.name

class Food(models.Model):
    # To be updated when crud operations on reservation are working
    food_name = models.CharField(max_length=100)

class Reservation(models.Model):
    
    reserver = models.ForeignKey('UserProfileInfo', related_name='reserver', on_delete=models.CASCADE)
    name = models.CharField(max_length=100,default="{} event".format(reserver))
    venue = models.ForeignKey('EventArea',related_name='eventarea',on_delete=models.CASCADE,default=1)
    package = models.ForeignKey('CateringPackage',related_name='package',on_delete=models.CASCADE)
    foodselections = models.CharField(max_length=1000,default="GM's Choice")
    event_type = models.CharField(max_length=100)
    currentdate = models.DateTimeField(auto_now=True)
    event_date = models.DateField()
    event_timestart = models.TimeField()
    event_timeend = models.TimeField()
    remarks = models.CharField(max_length=500)
    status = models.BooleanField(default=False)

    def completed(self):
        self.status = True
        self.save()

    def __str__(self):
        eventname = "{} {} ({})".format(str(self.reserver.user.first_name),self.event_type,self.reserver)
        return eventname
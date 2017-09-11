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

class Reservation(models.Model):
    
    reserver = models.ForeignKey('UserProfileInfo', related_name='reservers', on_delete=models.CASCADE)
    package = models.ForeignKey('CateringPackages',related_name='packages',on_delete=models.CASCADE)
    eventtype = models.CharField(max_length=100)
    currentdate = models.DateTimeField(auto_now=True)
    eventdate = models.DateTimeField()
    status = models.BooleanField(default=False)

    def __str__(self):
        eventname = "{} {} ({})".format(str(self.reserver.user.first_name),self.eventtype,self.reserver)
        return eventname
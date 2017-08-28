from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):
    
    user = models.OneToOneField(User)

    # please pip install pillow before using 
    # Image field
    profile_pic = models.ImageField(blank=True,upload_to='profile_pics')
    
    def __str__(self):
        return self.user.username

class CateringPackages(models.Model):
    
    name = models.CharField(max_length=100,blank=False)
    description = models.CharField(max_length=256,blank=False, null=False)
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.name
    
class Reservation(models.Model):
    
    reserver = models.ForeignKey('UserProfileInfo', related_name='reservers', on_delete=models.CASCADE)
    package = models.ForeignKey('CateringPackages',related_name='packages',on_delete=models.CASCADE)
    currentdate = models.DateTimeField(auto_now=True)
    targetdate = models.DateTimeField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.reserver
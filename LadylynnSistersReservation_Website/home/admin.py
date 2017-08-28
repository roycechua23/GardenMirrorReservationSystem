from django.contrib import admin
from home.models import UserProfileInfo, CateringPackages, Reservation

# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(CateringPackages)
admin.site.register(Reservation)
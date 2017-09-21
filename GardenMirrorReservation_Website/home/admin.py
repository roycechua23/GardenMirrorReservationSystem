from django.contrib import admin
from home.models import UserProfileInfo, CateringPackage, Reservation, EventArea, Food

# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(CateringPackage)
admin.site.register(EventArea)
admin.site.register(Food)
admin.site.register(Reservation)
from django.contrib import admin
from home.models import UserProfileInfo, CateringPackage, Reservation, EventArea, Food

# Register your models here.
class ReservationAdmin(admin.ModelAdmin):
    # fields = ['name','reserver','event_date','event_timestart','event_timeend','status']
    search_fields = ['name']
    list_filter = ['reserver','event_type','status']
    list_display = ['name','reserver','event_date','event_timestart','event_timeend','status']
    list_editable = ['status']

class CateringPackageAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name','pax','description','price']

admin.site.register(UserProfileInfo)
admin.site.register(CateringPackage,CateringPackageAdmin)
admin.site.register(EventArea)
admin.site.register(Food)
admin.site.register(Reservation,ReservationAdmin)

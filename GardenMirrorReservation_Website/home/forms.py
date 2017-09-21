from django import forms
from django.contrib.auth.models import User
from home.models import UserProfileInfo,CateringPackage,Reservation
# from django.forms import modelformset_factory

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    contact = forms.CharField()

    class Meta():
        model = User
        fields = ('first_name','last_name','email','contact','username','password')
        labels = {
            'email': 'Email Address',
            'contact': 'Contact Number (ex. 09061800313)'
        }

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('profile_pic',)

class ReservationForm(forms.ModelForm):
    # package = forms.MultipleChoiceField()
    # event_date = forms.DateTimeField(widget=forms.DateTimeInput(format=' %H:%M'),label="Event Date")
    # SplitDateTimeField(widget=forms.SplitDateTimeWidget(date_format='%m/%d/%Y',time_format='%H:%M'),label="Event Date")
    # reserver = forms.ModelChoiceField(queryset=UserProfileInfo.objects.all(),empty_label=None,label="Reserver")
    class Meta():
        model = Reservation
        fields = ('reserver','name','venue','package','event_type','foodselections','event_date','event_timestart','event_timeend')
        labels = {
            # labels for the html <label> equivalent
            'event_type': 'Event Type', 
            'event_date': 'Event Date',
            'event_timestart': 'Event Time Start',
            'event_timeend': 'Event Time End',
        }
        widgets = {
            # equivalent for the html attribute placeholder
            'event_date': forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD','id':"event_date"}),
            'event_timestart': forms.TimeInput(attrs={'placeholder': 'HH:MM','id':"event_timestart"}),
            'event_timeend': forms.TimeInput(attrs={'placeholder': 'HH:MM','id':"event_timeend"}),
        
        }

class UpdateForm(forms.ModelForm):
    # package = forms.MultipleChoiceField()
    # event_date = forms.DateTimeField(widget=forms.DateTimeInput(format=' %H:%M'),label="Event Date")
    # SplitDateTimeField(widget=forms.SplitDateTimeWidget(date_format='%m/%d/%Y',time_format='%H:%M'),label="Event Date")
    # reserver = forms.ModelChoiceField(queryset=UserProfileInfo.objects.all(),empty_label=None,label="Reserver")
    class Meta():
        model = Reservation
        fields = ('reserver','name','venue','package','event_type','foodselections','event_date','event_timestart','event_timeend')
        labels = {
            # labels for the html <label> equivalent
            'event_type': 'Event Type', 
            'event_date': 'Event Date',
            'event_timestart': 'Event Time Start',
            'event_timeend': 'Event Time End',
        }
        widgets = {
            # equivalent for the html attribute placeholder
            'event_date': forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD','id':"event_date"}),
            'event_timestart': forms.TimeInput(attrs={'placeholder': 'HH:MM','id':"event_timestart"}),
            'event_timeend': forms.TimeInput(attrs={'placeholder': 'HH:MM','id':"event_timeend"}),
        
        }


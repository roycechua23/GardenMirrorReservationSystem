from django import forms
from django.contrib.auth.models import User
from home.models import UserProfileInfo,CateringPackages,Reservation
from django.forms import modelformset_factory

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    contact = forms.CharField()

    class Meta():
        model = User
        fields = ('first_name','last_name','email','username','password')
        labels = {
            'email': 'Email Address'
        }

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('profile_pic',)

class ReservationForm(forms.ModelForm):
    # package = forms.MultipleChoiceField()
    # eventdate = forms.DateTimeField(widget=forms.DateTimeInput(format=' %H:%M'),label="Event Date")
    # SplitDateTimeField(widget=forms.SplitDateTimeWidget(date_format='%m/%d/%Y',time_format='%H:%M'),label="Event Date")
    # reserver = forms.ModelChoiceField(queryset=UserProfileInfo.objects.all(),empty_label=None,label="Reserver")

    class Meta():
        model = Reservation
        fields = ('reserver','package','eventtype','eventdate')
        labels = {
            'eventtype': 'Event Type',
            'eventdate': 'Event Date',
        }
        widgets = {
            'eventdate': forms.DateTimeInput(attrs={'placeholder': 'YYYY-MM-DD HH:MM:SS','id':"eventdate"}),
        }

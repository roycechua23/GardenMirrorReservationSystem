from django import forms
from django.contrib.auth.models import User
from home.models import UserProfileInfo,CateringPackage,Reservation
# from django.forms import modelformset_factory

class UserForm(forms.ModelForm):
    
    class Meta():
        model = User
        fields = ('first_name','last_name','username','password','email')
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Email Address'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Password'})
        }

    # def __init__(self, *args, **kwargs):
    #     super(UserForm, self).__init__(*args, **kwargs)
    #     self.fields.keyOrder = [
    #         'first_name',
    #         'last_name',
    #         'email',
    #         'username',
    #         'password']

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('contact','profile_pic',)
        labels = {
            'contact': 'Contact Number',
            'profile_pic': 'Profile Picture'
        }

class ReservationForm(forms.ModelForm):
    # package = forms.MultipleChoiceField()
    # event_date = forms.DateTimeField(widget=forms.DateTimeInput(format=' %H:%M'),label="Event Date")
    # SplitDateTimeField(widget=forms.SplitDateTimeWidget(date_format='%m/%d/%Y',time_format='%H:%M'),label="Event Date")
    # reserver = forms.ModelChoiceField(queryset=UserProfileInfo.objects.all(),empty_label=None,label="Reserver")
    class Meta():
        model = Reservation
        fields = ('reserver','name','venue','package','event_type','foodselections','event_date','event_timestart','event_timeend',"remarks")
        labels = {
            # labels for the html <label> equivalent
            'name': 'Event Name',
            'foodselections': 'Food Selections',
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
            'remarks': forms.Textarea(attrs={'placeholder':'You can write additional notes regarding your reservation here..'}),
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


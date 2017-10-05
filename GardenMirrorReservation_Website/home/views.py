from django.shortcuts import render,redirect
import requests
from datetime import *

from home.forms import UserForm,UserProfileInfoForm,ReservationForm, UpdateForm
from home.models import User,UserProfileInfo, CateringPackage, EventArea

from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
from home.forms import Reservation, CateringPackage

# for rest framework
from rest_framework import viewsets
from home.serializers import *


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class UserProfileInfoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = UserProfileInfo.objects.all()
    serializer_class = UserProfileInfoSerializer
# Create your views here.
# @csrf_exempt
# @api_view(['GET','POST'])
def index(request):
    user_form = UserForm()
    profile_form = UserProfileInfoForm()

    return render(request,"home/index.html",
                          context={'user_form':user_form,
                                   'profile_form':profile_form})

@require_http_methods(["POST"])
def register(request):

    registered = False

    if request.method == 'POST':

        # Get info from "both" forms
        # It appears as one form to the user on the .html page
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        # Check to see both forms are valid
        if user_form.is_valid() and profile_form.is_valid():

            # Save User Form to Database
            user = user_form.save()

            # Hash the password
            user.set_password(user.password)

            # Update with Hashed password
            user.save()

            # Now we deal with the extra info!

            # Can't commit yet because we still need to manipulate
            profile = profile_form.save(commit=False)

            # Set One to One relationship between
            # UserForm and UserProfileInfoForm
            profile.user = user

            # Check if they provided a profile picture
            if 'profile_pic' in request.FILES:
                print('found it')
                # If yes, then grab it from the POST form reply
                profile.profile_pic = request.FILES['profile_pic']

            # Now save model
            profile.save()

            # Registration Successful!
            registered = True

        else:
            # One of the forms was invalid if this else gets called.
            print(user_form.errors,profile_form.errors)

    else:
        # Was not an HTTP post so we just render the forms as blank.
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    # This is the render and context dictionary to feed
    # back to the body.html file page.
    return render(request,'home/body.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})

@require_http_methods(["POST"])
def user_login(request):
    
    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                u = User.objects.get(username=username)
                request.session['user_id'] = u.id
                request.session['user_username'] = u.username
                # return HttpResponseRedirect(reverse('home:user_home',args=[u.id]))
                return HttpResponseRedirect(reverse('home:user_home'))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("Someone tried to login and failed")
            print("Username: {} and password {}".format(username,password))
            return HttpResponse("Invalid Login details supplied")
    
    else:
        return HttpResponseRedirect(reverse('index'))

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def user_home(request):
    userinfo = User.objects.get(id=request.session['user_id'])
    userprofileinfo = UserProfileInfo.objects.get(user_id=request.session['user_id'])
    reservations = Reservation.objects.filter(reserver_id__user_id=request.session['user_id']).order_by('event_date')
    # print(reservations)
    # msg = "{} accessed dashboard.html".format(userinfo.username)
    # url = 'https://www.isms.com.my/isms_send.php?un=%s&pwd=%s&dstno=%d&msg=%s&type=1&sendid=GardenMirrorEventsPlace'%("royce236","261523",639060677392,msg)
    # txt = requests.get(url,proxies={"https":"http://proxy.server:3128"})
    return render(request,"home/dashboard.html",{'user':userinfo,'userprofilepic':userprofileinfo,'reservations':reservations})

@login_required
def loadmake_reservation(request):
    userinfo = User.objects.get(id=request.session['user_id'])
    userprofileinfo = UserProfileInfo.objects.get(user_id=request.session['user_id'])
    reservationform = ReservationForm()
    reservationform.fields['package'].empty_label=None
    reservationform.fields['reserver'].empty_label=None
    reservationform.fields['reserver'].queryset = UserProfileInfo.objects.filter(user__id=request.session['user_id'])
    packages=CateringPackage.objects.all()
    
    return render(request,"home/make_reservation.html",{'user':userinfo,'userprofilepic':userprofileinfo,'packages':packages,'reservationform':reservationform})

@login_required
def loadupdate_reservation(request):
    reservers = Reservation.objects.filter(reserver_id__user_id=request.session['user_id']).order_by('event_date')
    userinfo = User.objects.get(id=request.session['user_id'])
    userprofileinfo = UserProfileInfo.objects.get(user_id=request.session['user_id'])
    updateform = UpdateForm()
    updateform.fields['package'].empty_label=None
    updateform.fields['reserver'].empty_label=None
    updateform.fields['reserver'].queryset = UserProfileInfo.objects.filter(user__id=request.session['user_id'])
    packages=CateringPackage.objects.all()
    return render(request,"home/update_reservation.html",{'user':userinfo,'userprofilepic':userprofileinfo,'packages':packages,'updateform':updateform,'reservers':reservers})

@login_required
def retrieveEvent(request):
    event = request.GET.get('event', None)
    events = Reservation.objects.all()
    for e in events:
        if str(e)==event:
            print("Caught")
            p = CateringPackage.objects.get(name=str(e.package))
            v = EventArea.objects.get(name=e.venue)
            eventname = e.name
            venue = v.id
            package = p.id
            eventtype = str(e.event_type)
            foodselections = e.foodselections
            eventdate = e.event_date
            eventtimestart = time.strftime(e.event_timestart,"%I:%M %p")
            eventtimeend = time.strftime(e.event_timeend,"%I:%M %p")
            remarks = e.remarks
            # print(package,eventtype,eventdate,eventtimestart,eventtimeend)
            print(eventtimestart,eventtimeend)
        else:
            pass
    data = {
        'eventname': eventname,
        'venue': venue,
        'package':package,
        'eventtype':eventtype,
        'foodselections':foodselections,
        'eventdate':eventdate,
        'eventtimestart': eventtimestart,
        'eventtimeend': eventtimeend,
        'remarks':remarks,
    }
    return JsonResponse(data)

@login_required
def reserve(request):
    userinfo = User.objects.get(id=request.session['user_id'])
    userprofileinfo = UserProfileInfo.objects.get(user_id=request.session['user_id'])
    reservationform = ReservationForm()
    reservationform.fields['package'].empty_label=None
    reservationform.fields['reserver'].empty_label=None
    reservationform.fields['reserver'].queryset = UserProfileInfo.objects.filter(user__id=request.session['user_id'])

    if request.method == "POST":
        # this method is temporary, to be updated
        # with classbased views
        reservation = ReservationForm(data=request.POST)
        if reservation.is_valid():
            # print("Reservation happening")
            reservation.save()
            r = Reservation.objects.filter(name=request.POST.get('name')).order_by('currentdate')[0]
            eventtimestart = time.strftime(r.event_timestart,"%I:%M %p")
            eventtimeend = time.strftime(r.event_timeend,"%I:%M %p")
            # print(r.reserver)
            date_object = r.event_date
            eventdate = date_object.strftime('%B %d, %Y')
            u = User.objects.get(id=request.session['user_id'])
            # reserverfullinfo = str(u.first_name)+" "+str(u.last_name)+" ("+r.reserver+") "
            reserverfullinfo = r.reserver
            msg = "{} made a reservation\nContact Number: {}\nEvent name: {}\nEvent type: {}\nEvent date: {}\nStart time: {}\nEnd time: {}\nRemarks: {}\n--- end of message ---".format(reserverfullinfo,userprofileinfo.contact,r.name,r.event_type,eventdate,eventtimestart,eventtimeend,r.remarks)
            # print(msg)
            url = 'https://www.isms.com.my/isms_send.php?un=%s&pwd=%s&dstno=%d&msg=%s&type=1&sendid=GardenMirrorEventsPlace'%("royce236","261523",639060677392,msg)
            txt = requests.get(url,proxies={"https":"http://proxy.server:3128"})
            # print(txt)
            # requests.post('https://textbelt.com/text', {
            #     'phone': '+639060677392',
            #     'message': msg,
            #     'key': 'a336a88c21954636b8822431fe00ddcfd87cc670aehwDubgPTP8sHpi8yK9Jvli0',
            # })

            return HttpResponseRedirect(reverse('home:user_home'))
        else:
            print("Reservation did not proceed")
            return render(request, 'home/make_reservation.html', {'user':userinfo,'userprofilepic':userprofileinfo,'reservationform': reservationform})
    
    # if a GET (or any other method) we'll create a blank form
        reservation = ReservationForm(data=request.POST)
    else:
        reservationform = ReservationForm()

    return render(request, 'home/make_reservation.html', {'user':userinfo,'userprofilepic':userprofileinfo,'reservationform': reservationform})

@login_required
def update(request):
    if request.method == 'POST':
        r = Reservation.objects.get(name=request.POST.get('name'))
        reservation = UpdateForm(data=request.POST,instance=r)
        print(reservation.is_valid())
        if reservation.is_valid():
            reservation.save()
            print("Updated")
            return HttpResponseRedirect(reverse('home:user_home'))
    else:
        pass

    return HttpResponseRedirect(reverse('home:update_reservation'))

@login_required
def loadcancel_reservation(request):
    reservers = Reservation.objects.filter(reserver_id__user_id=request.session['user_id']).order_by('event_date')
    userinfo = User.objects.get(id=request.session['user_id'])
    userprofileinfo = UserProfileInfo.objects.get(user_id=request.session['user_id'])
    # updateform = UpdateForm()
    # updateform.fields['package'].empty_label=None
    # updateform.fields['reserver'].empty_label=None
    # updateform.fields['reserver'].queryset = UserProfileInfo.objects.filter(user__id=request.session['user_id'])
    # packages=CateringPackage.objects.all()
    return render(request,"home/cancel_reservation.html",{'user':userinfo,'userprofilepic':userprofileinfo,'reservers':reservers})

@login_required
def special(request):
    return HttpResponse("You are logged in, Nice!")

def rtest(request):
    return render(request,"home/index.html",context=None)


from django.conf.urls import url
from django.shortcuts import render
from django.http import HttpResponse


""" Add urls for home here """
from home import views

app_name = 'home'

urlpatterns = [
    url(r'^$',views.index,name="index"),
    url(r'^user_signup/$',views.register,name="user_signup"),
    url(r'^user_login/$',views.user_login,name="user_login"),
    url(r'^logout/$',views.user_logout,name="logout"),
    # url(r'^user_home/(?P<pk>[-\w]+)/$',views.user_home,name="user_home"),
    url(r'^user_home/$',views.user_home,name="user_home"),
    url(r'^make_reservation/$',views.loadmake_reservation,name="make_reservation"),
    url(r'^update_reservation/$',views.loadupdate_reservation,name="update_reservation"),
    url(r'^cancel_reservation/$',views.loadcancel_reservation,name="cancel_reservation"),
    url(r'^reserve/$',views.reserve,name="reserve"),
    url(r'^update/$',views.update,name="update"),
    url(r'^cancel/$',views.cancel,name="cancel"),
    url(r'^retrieveEvent/$',views.retrieveEvent,name="retrieveEvent"),
    url(r'^userprofile/$',views.userprofile,name="userprofile"),
    url(r'^sendemail/$',views.send_email, name="sendemail"),
    # url(r'api/users/$',views.UserViewSet,name="users"),
]
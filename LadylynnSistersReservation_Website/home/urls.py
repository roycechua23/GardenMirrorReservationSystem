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
    url(r'^user_home/(?P<pk>[-\w]+)/$',views.user_home,name="user_home"),
    url(r'^make_reservation/(?P<pk>[-\w]+)/$',views.loadmake_reservation,name="make_reservation")
]
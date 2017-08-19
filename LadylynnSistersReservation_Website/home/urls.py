from django.conf.urls import url
from django.shortcuts import render
from django.http import HttpResponse

""" Add urls for home here """
from home import views

urlpatterns = [
    url(r'^$',views.index)
]
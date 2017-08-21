from django.shortcuts import render
from home.forms import UserForm
# Create your views here.

def index(request):
    return render(request,"home/index.html",context=None)


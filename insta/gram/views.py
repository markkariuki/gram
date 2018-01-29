from django.shortcuts import render
from django.http  import HttpResponse
import datetime as db


# Create your views here.
def welcome(request):
    return render(request, 'home.html')

from django.http  import HttpResponse
import datetime as db


# Create your views here.
def welcome(request):
    return HttpResponse('Welcome to my gram which is being maintained will be back shortly')

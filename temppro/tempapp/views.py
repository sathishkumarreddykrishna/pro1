from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
import datetime as dt
def wellcome(request):
    f=get_template('welcome.html')
    return HttpResponse(f)
    
def contact(request):
    return HttpResponse("iam a very big fan of the jagan")
def about_us(request):
    z="yesterday india had lost the match because of some players bat is not good "
    return HttpResponse(z)
def current_time(request):
    date=dt.datetime.now()
    return HttpResponse(date)


from django.shortcuts import render
from django.http import HttpResponse
from .models import Home
def jobprofile(request):
    form=Home.objects.all()
    return render(request,'home.html',{'form':form})
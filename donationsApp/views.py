from django.shortcuts import render
from django.http import HttpResponse
from .models import Donations
from django.utils import translation

def index(request):
    return HttpResponse("Hello Geeks")

def say_hello(request):
    return render(request, 'hello.html', {'name': 'Abhishek'})

def donation_list(request):
    donations = Donations.objects.all()
    translation.activate('en_IN')
    context = {'donations': donations}
    return render(request, 'donations.html', context)


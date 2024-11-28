from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def captain(request):
    return HttpResponse('<h1> King kohli is captain of rcb </h1>')

def vicecaptain(request):
    return HttpResponse('<h1> hazelwood is the vice captain of rcb</h1>')
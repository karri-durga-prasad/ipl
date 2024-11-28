from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def captain(request):
    return HttpResponse('<h1> rutraj is the captain of csk </h1>')

def vicecaptain(request):
    return HttpResponse()
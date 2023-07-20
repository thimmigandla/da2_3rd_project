from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def string_response(request):
    return HttpResponse('This is my first project file')
def second_response(request):
    return HttpResponse('this is my sencond response file')

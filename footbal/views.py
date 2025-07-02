from django.shortcuts import render
from django.http import HttpResponse

def say_hello(request):
    return HttpResponse('this is a demo change ...')


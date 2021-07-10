from django.http.response import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render

# Create your views here.
from django.http import HttpRequest

from django.http import HttpResponse

def home(request):
    return HttpRequest("hello world")
    
from django.shortcuts import render

# Create your views here.
# cal/views.py

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('hello')
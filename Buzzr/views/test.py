from django.shortcuts import render
from django.http import HttpResponse

def test_webpage(request):
    return HttpResponse("Hello World!")
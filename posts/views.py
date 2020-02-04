from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# the logic handle the request the browser/client make
def post_home(request):
    return HttpResponse("<h1>Hello</h1>")

from django.shortcuts import render,HttpResponse

# Create your views here.

def first(request):
    return HttpResponse("Hey i am Fisrt Demo app")
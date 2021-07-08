from django.shortcuts import render,HttpResponse
from .models import index

# Create your views here.s
def first(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = index(name=name, email=email, password=password)
        user.save()
    return render(request, 'index.html', {'name' : 'Akshit Joshi'})
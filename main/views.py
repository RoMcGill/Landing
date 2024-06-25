
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def getStarted(request):
    return render(request, 'get-started.html')

def work(request):
    return render(request, 'work.html')
from django.shortcuts import render

# Create your views here.

def index(request):
    """Home page for hotel app"""
    return render(request, 'crunchy_home/index.html')
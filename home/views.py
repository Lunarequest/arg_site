from django.shortcuts import render, redirect
from django.contrib.auth import  authenticate
# Create your views here.
def home(request):
    if request.method=="POST":
        username = request.POST['username']
        passwd = request.POST['passwd']
        user = authenticate(username=username, password=passwd)
        if user:
            redirect('downloads')
            
    else:
        response = render(request, "home/home.html")
        return response
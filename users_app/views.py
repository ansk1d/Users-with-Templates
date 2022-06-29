from django.shortcuts import render, redirect
from .models import *

def index(request):
    allusers = users.objects.all()
    context = {
        "users":allusers,
    }
    return render(request, 'index.html',context)

def adduser(request):
    user = users.objects.create(
        fname = request.POST['fname'],
        lname = request.POST['lname'],
        email = request.POST['email'],
        age = request.POST['age'],
    )
    user.save()
    return redirect("/")

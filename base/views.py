from django.shortcuts import render
from django.http import HttpResponse 
from .models import Room
# Create your views here.

def home(request):
    room = Room.objects.all()
    context = {"rooms":room}
    return render(request,"main.html",context)

def room(request,pk):
    room = Room.objects.get(id = int(pk))
    context = {"rooms":room}
    return render(request,"room.html",context)


from django.shortcuts import render
from rooms.models import Room

# Create your views here.
def list_rooms(request):
    rooms = Room.objects.all()
    print(rooms)
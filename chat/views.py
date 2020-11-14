from django.shortcuts import render
from django.http import HttpResponse as HR
def index(req):
    return render(req, 'chat/index.html')

def room(req, room_name):
    return render(req, 'chat/room.html', {
        'room_name': room_name
    })
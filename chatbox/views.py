from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import json
from django.utils.safestring import mark_safe

# Create your views here.

def home(request):
    return render(request, 'chatbox/home.html')


def index(request):
    return render(request, 'chatbox/index.html')

@login_required
def room(request, room_name):
    return render(request, 'chatbox/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name)),
        'username': mark_safe(json.dumps(request.user.username)),
    })
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest

def index(request)->HttpResponse:
	if request.user.is_authenticated:
		return render(request, 'chat/index.html', {})
	else:
		return redirect('account')


def room(request, room_name)->HttpResponse:
	if request.user.is_authenticated:
		return render(request, 'chat/room.html', {
        'room_name': room_name
    })
	else:
		return redirect('account')

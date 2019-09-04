from django.shortcuts import render
from django.contrib.auth.models import User

from .models import Message


def chat_list(request):
	chat_list = User.objects.filter()
	return render(request, 'chat/chat_list.html', {'chats': chat_list})

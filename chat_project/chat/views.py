from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import Message


@login_required
def chat_list(request):
    # cur_user = request.user
    # print(cur_user)
    chat_list = User.objects.filter()
    return render(request, 'chat/chat_list.html', {'chats': chat_list})

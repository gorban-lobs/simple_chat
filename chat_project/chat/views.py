from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import Message


@login_required
def chat_list(request):
    cur_user_id = str(request.user.id)
    query = '''
            SELECT u.id, username, count(m.sender_id) as cnt
            FROM auth_user u LEFT JOIN chat_message m ON
            u.id = m.sender_id AND  m.is_red = False AND m.getter_id = %s
            GROUP BY u.id HAVING u.id <> %s
            '''
    chat_list = User.objects.raw(query, (cur_user_id, cur_user_id))
    return render(request, 'chat/chat_list.html', {'chats': chat_list})


@login_required
def chat_page(request, pk):
    return render(request, 'chat/chat_page.html')

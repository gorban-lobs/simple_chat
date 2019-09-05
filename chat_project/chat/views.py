from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from .models import Message


@login_required
def chat_list(request):
    cur_user_id = request.user.id
    query = '''
            SELECT u.id, username, count(m.sender_id) as cnt
            FROM auth_user u LEFT JOIN chat_message m ON
            u.id = m.sender_id AND  m.is_red = False AND m.getter_id = %s
            GROUP BY u.id HAVING u.id <> %s
            '''
    chat_list = User.objects.raw(query, (str(cur_user_id), str(cur_user_id)))
    return render(request=request,
                  template_name='chat/chat_list.html',
                  context={'chats': chat_list})


@login_required
def chat_page(request, pk):
    cur_user_id = request.user.id

    if request.method == 'GET':
        Message.objects.filter(sender_id=pk,
                               getter_id=cur_user_id,
                               is_red=False).update(is_red=True)

    if request.method == 'POST':
        print(request.POST)
        new_message = Message(sender_id=cur_user_id, getter_id=pk,
                              text=request.POST['message'])
        new_message.send()

    query = query = '''
        SELECT id, sender_id, getter_id, sended_time, text
        FROM chat_message
        WHERE sender_id = %s AND getter_id = %s OR
        sender_id = %s AND getter_id = %s
        '''
    history = Message.objects.raw(query,
                                  (str(cur_user_id), pk, pk, str(cur_user_id)))

    return render(request=request,
                  template_name='chat/chat_page.html',
                  context={'history': history, 'cur_id': cur_user_id})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            return redirect('chat_list')
        else:
            return render(request=request,
                          template_name="registration/registration.html",
                          context={"form": form})

    form = UserCreationForm
    return render(request=request,
                  template_name="registration/registration.html",
                  context={"form": form})

from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def get_all_chats(request):
    user = request.user
    chats = Chat.objects.filter(users__username=user.username).order_by('name')
    if user.is_agent is False:
        return render(request,'chats/display_chats.html',{'chats':chats})
    else:
        data = []
        for chat in chats:
            context = {}
            context['name'] = chat.name
            context['slug'] = chat.slug
            for chat_user in chat.users.all():
                if chat_user.is_agent is False:
                    context['user_id'] = chat_user.user_id
            data.append(context)
        return render(request,'chats/display_chats.html',{'chats':data})

@login_required
def enter_chat(request,slug):
    chat = Chat.objects.get(slug=slug)
    messages = Message.objects.filter(chat=chat)[:25]
    if request.user.is_agent is False:
        return render(request,'chats/single_chat.html',{'chat':chat, 'messages':messages})
    else:
        context = {}
        context['name'] = chat.name
        context['slug'] = chat.slug
        for chat_user in chat.users.all():
            if chat_user.is_agent is False:
                context['user_id'] = chat_user.user_id
        return render(request,'chats/single_chat.html',{'chat':context, 'messages':messages})
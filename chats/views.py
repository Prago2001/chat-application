from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def get_all_chats(request):
    chats = Chats.objects.all()
    return render(request,'chats/display_chats.html',{'chats':chats})

@login_required
def enter_chat(request,slug):
    chat = Chats.objects.get(slug=slug)
    return render(request,'chats/single_chat.html',{'chat':chat})
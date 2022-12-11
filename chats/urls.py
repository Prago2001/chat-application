from django.urls import path
from .views import *

urlpatterns = [
    path('',view=get_all_chats,name='chats'),
    path('<slug:slug>/',view=enter_chat,name='chat')
]
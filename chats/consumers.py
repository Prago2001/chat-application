import json
from .models import *
# from django.contrib.auth.models import User
from django.conf import settings
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
# User = settings.AUTH_USER_MODEL
from core.models import User

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.chat_slug = self.scope['url_route']['kwargs']['chat_slug']
        self.chat_group_name = 'chat_%s' % self.chat_slug

        await self.channel_layer.group_add(
            self.chat_group_name,
            self.channel_name
        )
        
        await self.accept()
    
    async def disconnect(self,close_code):
        await self.channel_layer.group_discard(
            self.chat_group_name,
            self.channel_name
        )
    
    async def receive(self, text_data):
        data = json.loads(text_data)
        print(data)
        message = data['message']
        username = data['username']
        chat = data['chat']

        await self.save_message(username, chat, message)

        await self.channel_layer.group_send(
            self.chat_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': username
            }
        )
    
    async def chat_message(self, event):
        message = event['message']
        username = event['username']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'username': username
        }))
    
    @sync_to_async
    def save_message(self, username, chat, message):
        user = User.objects.get(username=username)
        chat = Chat.objects.get(slug=chat)

        Message.objects.create(user=user, chat=chat, content=message)
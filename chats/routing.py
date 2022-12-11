from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/<int:chat_slug>/',consumers.ChatConsumer.as_asgi())
]
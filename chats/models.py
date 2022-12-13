from django.db import models
# from django.contrib.auth.models import User
# from django.conf import settings
# User = settings.AUTH_USER_MODEL
from core.models import User
import datetime as dt

# Create your models here.
class Chat(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    users = models.ManyToManyField(User)

    def __str__(self) -> str:
        return self.name

class Message(models.Model):
    chat = models.ForeignKey(Chat,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(null=True)

    def save(self,*args,**kwargs):
        if self.timestamp is None:
            self.timestamp = dt.datetime.now()
        super(Message,self).save(*args,**kwargs)

    class Meta:
        ordering = ('timestamp',)
    
    def __str__(self) -> str:
        return self.chat.name + "->" + self.user.username
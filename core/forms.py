# from django.contrib.auth.forms import UserCreationForm, User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from .models import User

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','password1', 'password2')

class CustomUserChangeForm(UserChangeForm):
    user_id = forms.IntegerField(label='User ID')
    is_agent = forms.BooleanField(label='Is Agent',required=False)
    class Meta:
        model = User
        fields = ('username','user_id','is_agent')
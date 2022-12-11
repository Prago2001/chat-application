from django.contrib.auth.forms import UserCreationForm, User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
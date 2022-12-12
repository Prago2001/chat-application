from django.contrib import admin
from .models import *
# Register your models here.
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ["username",'user_id','is_agent']
    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('user_id','is_agent')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
            (None, {'fields': ('user_id','is_agent')}),
    )

admin.site.register(User, CustomUserAdmin)

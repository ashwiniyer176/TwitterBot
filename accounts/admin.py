from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import forms, models
# Register your models here.


class CustomUserAdmin(UserAdmin):
    add_form = forms.CustomUserCreationForm
    form = forms.CustomUserChangeForm
    model = models.CustomUser
    list_display = ['email', 'username']


admin.site.register(models.CustomUser, CustomUserAdmin)

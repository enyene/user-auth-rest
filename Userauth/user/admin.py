from django.contrib import admin
from . import models
from django.contrib.auth.admin import UserAdmin
from . import forms
# Register your models here.

@admin.register(models.CustomerUser)
class CustomerUserAdmin(UserAdmin):
    add_form = forms.CustomerUserCreationForm
    form = forms.CustomerUserChangeForm
    list_display = ['email', 'is_superuser', 'is_active', 'is_staff']
    ordering = ['email']
    fieldsets = (
                (None, {'fields': ('email', 'password','username')}),
                ('Details', {'fields': ('first_name', 'last_name','slug')}),
                ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')})
                )
    search_fields = ('email',)
    
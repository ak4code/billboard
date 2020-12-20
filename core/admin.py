from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import AccountCreationForm, AccountChangeForm
from .models import Account


@admin.register(Account)
class AccountAdmin(UserAdmin):
    add_form = AccountCreationForm
    form = AccountChangeForm
    model = Account
    list_display = ('email', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        ('Основные', {'fields': ('email', 'password')}),
        ('Настройки', {'fields': ('is_staff', 'is_active')}),
        ('Личные данные', {'fields': ('first_name', 'last_name', 'phone')}),
        ('Права доступа', {'fields': ('groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)

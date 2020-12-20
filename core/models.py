from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

from .managers import AccountManager


class Account(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name='Email', unique=True)
    is_staff = models.BooleanField(verbose_name='Доступ в админ-панель', default=False)
    is_active = models.BooleanField(verbose_name='Активный', default=True)
    first_name = models.CharField(blank=True, max_length=30, verbose_name='Имя')
    last_name = models.CharField(blank=True, max_length=150, verbose_name='Фамилия')
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name='Телефон', unique=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = AccountManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Аккаунт'
        verbose_name_plural = 'Аккаунты'

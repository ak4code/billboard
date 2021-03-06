from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.base_user import BaseUserManager


class AccountManager(BaseUserManager):
    """
    Кастомный менеджер модели, где электронная почта является уникальным идентификатором.
    для аутентификации вместо имени пользователя.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Создать и сохранить Пользоваиеля использую email и пароль.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Создать и сохранить Супер-Пользователя используя email и пароль.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)
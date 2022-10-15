from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models


ROLES = [
    ('user', 'Аутентифицированный пользователь'),
    ('moderator', 'Модератор'), ('admin', 'Администратор'),
    ('superuser', 'Суперюзер Django')
]


class User(AbstractUser):
    """Кастомная модель пользователя"""
    USER = 'user'
    MODERATOR = 'moderator'
    ADMIN = 'admin'

    username = models.CharField(max_length=150, unique=True,
                                validators=[UnicodeUsernameValidator],)
    email = models.EmailField(max_length=254, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    bio = models.TextField(blank=True)
    role = models.CharField(
        choices=ROLES, max_length=35, default='user'
    )
    confirmation_code = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.username

    @property
    def is_user(self):
        return self.role == self.USER

    @property
    def is_moderator(self):
        return self.role == self.MODERATOR

    @property
    def is_admin(self):
        return self.role == self.ADMIN

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'role', 'confirmation_code']

from django.db import models
from django.contrib.auth.models import AbstractUser

NULLABLE = {"blank": True, "null": True}
Permissions = [('View_the_list_of_service_users', 'Просматривать список пользователей сервиса'),
               ('Block_users_of_the_service', 'Блокировать пользователей сервиса'), ]


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Электронная почта')
    phone = models.CharField(max_length=30, verbose_name='Контактный телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='Автар', **NULLABLE)
    country = models.CharField(max_length=40, verbose_name='Страна', **NULLABLE)
    token = models.CharField(max_length=100, verbose_name='Токен', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.email}"

    class Meta:
        db_table = "user"
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ("email",)
        permissions = Permissions

from django.db import models
from django.contrib.auth.models import AbstractUser

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')
    phone = models.CharField(max_length=30, verbose_name='телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='автар', **NULLABLE)
    country = models.CharField(max_length=40, verbose_name='страна')
    token = models.CharField(max_length=100, verbose_name='токен', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.email}"

    class Meta:
        db_table = "user"
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"
        ordering = ("email",)

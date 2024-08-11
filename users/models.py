from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {"null": True, "blank": True}


class User(AbstractUser):
    """ Модель Пользователя """

    username = None
    email = models.EmailField(unique=True, verbose_name="email")
    phone = models.CharField(max_length=35, **NULLABLE, verbose_name="phone")
    avatar = models.ImageField(upload_to="user/", **NULLABLE, verbose_name="avatar")
    city = models.CharField(max_length=100, **NULLABLE, verbose_name="city")
    token = models.CharField(max_length=100, **NULLABLE, verbose_name="token")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.email}"

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

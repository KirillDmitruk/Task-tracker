from django.contrib.auth.models import AbstractUser
from django.db import models

from task_tracker.models import Task

NULLABLE = {"null": True, "blank": True}


class Position(models.Model):
    name = models.CharField(max_length=150, verbose_name='наименование')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'должность'
        verbose_name_plural = 'должности'


class User(AbstractUser):
    """ Модель Пользователя """

    username = None
    email = models.EmailField(unique=True, verbose_name="email")
    phone = models.CharField(max_length=35, **NULLABLE, verbose_name="phone")
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, verbose_name='должность', **NULLABLE)
    tasks = models.ManyToManyField(Task, verbose_name='задачи', blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.email}"

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

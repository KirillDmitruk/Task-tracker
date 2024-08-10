from django.db import models

from employee.models import Employee

NULLABLE = {'blank': True, 'null': True}


class Task(models.Model):
    """Model of Task."""
    name = models.CharField('Наименование задачи', max_length=200)
    executor = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name='Исполнитель')
    deadline = models.DateField('Срок выполнения')
    status = models.CharField('Статус', max_length=100)
    description = models.TextField('Описание', **NULLABLE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

from django.db import models

from employee.models import Employee

NULLABLE = {'blank': True, 'null': True}


class Task(models.Model):
    """Model of Task."""

    CREATED = 'Создана'
    IN_WORK = 'В работе'
    COMPLETED = 'Завершена'

    STATUS = (
        (CREATED, 'Создана'),
        (IN_WORK, 'В работе'),
        (COMPLETED, 'Завершена'),
    )

    name = models.CharField('Наименование задачи', max_length=200)
    executor = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name='Исполнитель')
    deadline = models.DateField('Срок выполнения')
    status = models.CharField('Статус', max_length=100, choices=STATUS, **NULLABLE)
    description = models.TextField('Описание', **NULLABLE)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True, **NULLABLE)
    updated_at = models.DateTimeField('Дата изменения', auto_now=True, **NULLABLE)
    parent_task = models.ForeignKey('self', on_delete=models.SET_NULL, **NULLABLE)
    is_taken = models.BooleanField('Взят ли в работу', default=False, **NULLABLE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

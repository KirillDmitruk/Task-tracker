from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Employee(models.Model):
    """Model of Employee."""
    first_name = models.CharField('Имя', max_length=150)
    last_name = models.CharField('Фамилия', max_length=150)
    middle_name = models.CharField('Отчество', max_length=150)
    position = models.CharField('Должность', max_length=150)

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.middle_name}'

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

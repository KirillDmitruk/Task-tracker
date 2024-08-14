from django.db import models


NULLABLE = {'null': True, 'blank': True}


class Status(models.Model):
    STATUS = (
        ('open', 'открыта'),
        ('in_progress', 'в процессе'),
        ('resolved', 'решена'),
        ('closed', 'закрыта'),
    )
    name = models.CharField(max_length=200, verbose_name='наименование', choices=STATUS)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class Task(models.Model):
    name = models.CharField(max_length=200, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, verbose_name='статус', **NULLABLE)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, verbose_name='родитель', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'задача'
        verbose_name_plural = 'задачи'

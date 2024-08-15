from django.db import models

NULLABLE = {"null": True, "blank": True}


class Employee(models.Model):
    full_name = models.CharField("ФИО", max_length=150)
    position = models.CharField("Должность", max_length=100)
    vacation_status = models.BooleanField("Статус нахождения в отпуске/на выходном/ на больничном",
                                          default=False)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"


class Task(models.Model):
    STATUS_DONE = "done"
    STATUS_IN_PROGRESS = "in_progress"
    STATUS_NOT_STARTED = "not_started"
    STATUS = [
        (STATUS_DONE, "Выполнено"),
        (STATUS_IN_PROGRESS, "В процессе выполнения"),
        (STATUS_NOT_STARTED, "Не приступал к выполнению"),
    ]

    title = models.CharField("Название задачи", max_length=255)
    parent_task = models.ForeignKey("self", on_delete=models.CASCADE, **NULLABLE, verbose_name="Родительская задача")
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name="Иcполнитель")
    start_date = models.DateField("Дата начала")
    end_date = models.DateField("Дата окончания")
    status = models.CharField("Статус", max_length=20, choices=STATUS, default=STATUS_NOT_STARTED)
    comments = models.TextField("Комментарии к задаче", **NULLABLE)
    owner = models.TextField("создатель", **NULLABLE)
    is_active = models.BooleanField("Признак активности задачи", default=True)
    is_important = models.BooleanField("Признак важности задачи", default=False)

    def __str__(self):
        return f"{self.title}: {self.status}"

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"

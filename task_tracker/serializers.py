from django.db.models import Q
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from rest_framework.serializers import UniqueTogetherValidator

from task_tracker.models import Employee, Task
from task_tracker.validators import TitleValidator


class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"


class EmployeeActiveTasksSerializer(ModelSerializer):
    count_active_tasks = SerializerMethodField()
    tasks = SerializerMethodField()

    def get_count_active_tasks(self, employee):
        return Task.objects.filter(Q(employee=employee.id), Q(is_active=True)).count()

    def get_tasks(self, employee):
        tasks = Task.objects.filter(employee=employee.id)
        tasks_list = []
        for task in tasks:
            if task.is_active:
                tasks_list.append(task.title)
        return tasks_list

    class Meta:
        model = Employee
        fields = ("full_name", "tasks", "count_active_tasks")


class TaskSerializer(ModelSerializer):
    term_days = SerializerMethodField()

    def get_term_days(self, task):
        if task.end_date and task.start_date:
            return (task.end_date - task.start_date).days

    class Meta:
        model = Task
        fields = "__all__"
        validators = [
            TitleValidator(field="title"),
            UniqueTogetherValidator(fields=["title"], queryset=Task.objects.all()),
        ]


class ImportantTaskSerializer(ModelSerializer):
    available_employees = SerializerMethodField()

    def get_current_employees(self, task):
        employees_task = Task.objects.filter(id=task.id)
        employees_list = []
        for task in employees_task:
            employees_list.append(task.employee.full_name)
        return employees_list

    def get_term_days(self, task):
        if task.end_date and task.start_date:
            return (task.end_date - task.start_date).days

    def get_parent_task_title(self, task):
        return task.parent_task.title

    def get_available_employees(self, task):
        employees = Employee.objects.all()
        emp_data = {}
        available_employees = []
        # ищем наименее загруженного сотрудника
        for emp in employees:
            list_task = emp.task_set.all()
            emp_data[emp.pk] = len(list_task)
        min_count = min(emp_data.values())
        if task.employee.full_name not in available_employees:
            available_employees = [
                emp.full_name for emp in employees if emp_data[emp.pk] == min_count
            ]
        # ищем подходящего сотрудника, выполняющего родительскую задачу
        for emp in employees:
            tasks = emp.task_set.all()
            for t in tasks:
                if (
                        task.parent_task == t.parent_task
                        and len(tasks) - min_count <= 2
                        and emp.full_name not in available_employees
                ):
                    available_employees.append(emp.full_name)
        return available_employees

    class Meta:
        model = Task
        fields = (
            "title",
            "end_date",
            "available_employees",
        )

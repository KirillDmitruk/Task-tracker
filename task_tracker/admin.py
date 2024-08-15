from django.contrib import admin

from task_tracker.models import Employee, Task


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'position', 'vacation_status',)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title', 'parent_task', 'employee', 'start_date', 'end_date', 'status', 'comments', 'owner', 'is_active',
        'is_important',)

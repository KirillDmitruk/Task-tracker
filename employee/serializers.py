from rest_framework import serializers

from employee.models import Employee
from task.serializers import TaskSerializer


class EmployeeSerializer(serializers.ModelSerializer):
    """Serializer for model Employee."""
    tasks = TaskSerializer(many=True, read_only=True)
    active_task_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Employee
        fields = ('first_name', 'last_name', 'middle_name', 'position', 'tasks', 'active_task_count')

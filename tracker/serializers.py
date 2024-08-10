from rest_framework import serializers

from tracker.models import Employee, Task


class EmployeeSerializer(serializers.ModelSerializer):
    """Serializer for model Employee."""

    class Meta:
        model = Employee
        fields = ('first_name', 'last_name', 'middle_name', 'position')


class TaskSerializer(serializers.ModelSerializer):
    """Serializer for model Task."""

    class Meta:
        model = Task
        fields = ('name', 'executor', 'deadline', 'status', 'description')


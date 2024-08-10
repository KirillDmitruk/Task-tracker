from rest_framework import serializers

from employee.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    """Serializer for model Employee."""

    class Meta:
        model = Employee
        fields = ('first_name', 'last_name', 'middle_name', 'position')

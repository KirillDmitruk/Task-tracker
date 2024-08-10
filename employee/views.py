from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from employee.models import Employee
from employee.serializers import EmployeeSerializer


class EmployeeCreateAPIView(CreateAPIView):
    """Create an employee instance."""
    serializer_class = EmployeeSerializer


class EmployeeListAPIView(ListAPIView):
    """List all users."""
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeRetrieveAPIView(RetrieveAPIView):
    """Retrieve a user instance."""
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeUpdateAPIView(UpdateAPIView):
    """Update a user instance."""
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeDestroyAPIView(DestroyAPIView):
    """Delete a user instance."""
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

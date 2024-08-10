from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from tracker.models import Employee, Task
from tracker.serializers import EmployeeSerializer, TaskSerializer


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


class TaskCreateAPIView(CreateAPIView):
    """Create a task instance."""
    serializer_class = TaskSerializer


class TaskListAPIView(ListAPIView):
    """List all tasks."""
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskRetrieveAPIView(RetrieveAPIView):
    """Retrieve a task instance."""
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskUpdateAPIView(UpdateAPIView):
    """Update a task instance."""
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDestroyAPIView(DestroyAPIView):
    """Delete a task instance."""
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

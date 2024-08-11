from django.db.models import Count, Q
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


class BusyEmployeesView(ListAPIView):
    """List all users with tasks in progress or completed."""
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        return Employee.objects.annotate(
            active_task_count=Count('tasks', filter=Q(tasks__status='IN_WORK'))
        ).order_by('-active_task_count')


class LeastBusyEmployeeView(RetrieveAPIView):
    """View to get the least busy employee."""
    serializer_class = EmployeeSerializer

    def get_object(self):
        # Получить наименее занятого сотрудника
        return Employee.objects.annotate(
            active_task_count=Count('tasks', filter=Q(tasks__status='IN_WORK'))
        ).order_by('active_task_count').first()


class EmployeeForParentTaskView(RetrieveAPIView):
    """View to get employee working on a parent task."""
    serializer_class = EmployeeSerializer

    def get_object(self):
        parent_task_id = self.kwargs.get('parent_task_id')
        return Employee.objects.filter(tasks__id=parent_task_id).distinct().first()

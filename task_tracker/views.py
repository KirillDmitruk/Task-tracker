from django.db.models import Q, Count
from rest_framework.filters import SearchFilter
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
)

from task_tracker.models import Employee, Task
from task_tracker.serializers import (
    EmployeeSerializer,
    TaskSerializer,
    ImportantTaskSerializer,
    EmployeeActiveTasksSerializer,
)


class TaskCreateAPIView(CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        task = serializer.save()
        task.owner = self.request.user
        task.save()


class TaskListAPIView(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class ImportantTaskListAPIView(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = ImportantTaskSerializer

    def get_queryset(self):
        self.queryset = Task.objects.filter(
            Q(status=Task.STATUS_NOT_STARTED),
            Q(is_important=True),
            Q(parent_task__status=Task.STATUS_IN_PROGRESS),
        )
        return self.queryset


class TaskRetrieveAPIView(RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskUpdateAPIView(UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDestroyAPIView(DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class EmployeeCreateAPIView(CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeListAPIView(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeActiveTasksListAPIView(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeActiveTasksSerializer
    filter_backends = [SearchFilter]
    search_fields = ["full_name"]

    def get_queryset(self):
        self.queryset = Employee.objects.all()
        self.queryset = self.queryset.select_related()
        self.queryset = Employee.objects.annotate(tasks_count=Count("task")).order_by(
            "-tasks_count"
        )
        return self.queryset


class EmployeeRetrieveAPIView(RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeActiveTasksSerializer


class EmployeeUpdateAPIView(UpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeDestroyAPIView(DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

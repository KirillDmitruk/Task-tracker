from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response

from task.models import Task
from task.serializers import TaskSerializer
from django.db.models import Q


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


class TaskImportantView(ListAPIView):
    """List all important tasks."""
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(Q(status='В работе') | Q(status='Завершена')).distinct()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        data = [
            {'name': task.name, 'executor': task.executor.last_name, 'deadline': task.deadline}
            for task in queryset
        ]

        return Response(data)


class TaskUpdateAPIView(UpdateAPIView):
    """Update a task instance."""
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDestroyAPIView(DestroyAPIView):
    """Delete a task instance."""
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

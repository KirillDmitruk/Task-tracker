from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from task.models import Task
from task.serializers import TaskSerializer


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

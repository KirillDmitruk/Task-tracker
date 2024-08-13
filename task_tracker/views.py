from rest_framework import generics
from task_tracker.models import Status, Task
from task_tracker.serializers import StatusSerializer, TaskSerializer


class StatusCreateAPIView(generics.CreateAPIView):
    serializer_class = StatusSerializer
    queryset = Status.objects.all()


class StatusListAPIView(generics.ListAPIView):
    serializer_class = StatusSerializer
    queryset = Status.objects.all()


class StatusUpdateAPIView(generics.UpdateAPIView):
    serializer_class = StatusSerializer
    queryset = Status.objects.all()


class StatusDestroyAPIView(generics.DestroyAPIView):
    serializer_class = StatusSerializer
    queryset = Status.objects.all()


class StatusRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = StatusSerializer
    queryset = Status.objects.all()


class TaskCreateAPIView(generics.CreateAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class TaskListAPIView(generics.ListAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class TaskUpdateAPIView(generics.UpdateAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class TaskDestroyAPIView(generics.DestroyAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class TaskRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class ImportantTasksListAPIView(generics.ListAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        queryset = Task.objects.filter(user__id=None, parent__isnull=False)
        return queryset

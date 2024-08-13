from django.db.models import Count
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from task_tracker.models import Task
from users.models import User, Position
from users.serializers import (
    UserSerializer,
    PositionSerializer,
    EmployedUserSerializer
)


class PositionCreateAPIView(generics.CreateAPIView):
    serializer_class = PositionSerializer
    queryset = Position.objects.all()


class PositionListAPIView(generics.ListAPIView):
    serializer_class = PositionSerializer
    queryset = Position.objects.all()


class PositionUpdateAPIView(generics.UpdateAPIView):
    serializer_class = PositionSerializer
    queryset = Position.objects.all()


class PositionDestroyAPIView(generics.DestroyAPIView):
    serializer_class = PositionSerializer
    queryset = Position.objects.all()


class PositionRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = PositionSerializer
    queryset = Position.objects.all()


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserListAPIView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserUpdateAPIView(generics.UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDestroyAPIView(generics.DestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class EmployedUsersListAPIView(generics.ListAPIView):
    serializer_class = EmployedUserSerializer
    queryset = User.objects.filter(tasks__id__isnull=False).annotate(task_count=Count('tasks')).order_by(
        'task_count').distinct()


class AvailableUserForTaskRetrieveAPIView(APIView):

    def get(self, request, pk):

        user_min_task = User.objects.all().annotate(task_count=Count('tasks')).order_by('task_count').first()

        task_parent = Task.objects.get(pk=pk).parent
        user_task_parent = User.objects.filter(tasks__id=task_parent.id).first()

        count_user_task_parent = len(list(user_task_parent.tasks.all()))
        count_user_min_task = len(list(user_min_task.tasks.all()))
        if count_user_task_parent - count_user_min_task <= 2:
            queryset = User.objects.filter(pk=user_task_parent.pk)
        else:
            queryset = User.objects.filter(pk=user_min_task.pk)

        serializer = UserSerializer(queryset, many=True)

        return Response(serializer.data)

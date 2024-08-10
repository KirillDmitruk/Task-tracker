from django.urls import path

from task.apps import TaskConfig
from task.views import TaskCreateAPIView, TaskListAPIView, TaskRetrieveAPIView, TaskUpdateAPIView, \
    TaskDestroyAPIView

app_name = TaskConfig.name

urlpatterns = [
    path('create/', TaskCreateAPIView.as_view(), name='task_create'),
    path('', TaskListAPIView.as_view(), name='task_list'),
    path('<int:pk>/', TaskRetrieveAPIView.as_view(), name='task_detail'),
    path('update/<int:pk>/', TaskUpdateAPIView.as_view(), name='task_update'),
    path('delete/<int:pk>/', TaskDestroyAPIView.as_view(), name='task_delete')
]

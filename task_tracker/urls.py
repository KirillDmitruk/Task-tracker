from django.urls import path

from task_tracker.apps import TaskTrackerConfig
from task_tracker.views import (
    StatusCreateAPIView,
    StatusListAPIView,
    StatusUpdateAPIView,
    StatusDestroyAPIView,
    StatusRetrieveAPIView,
)
from task_tracker.views import (
    TaskCreateAPIView,
    TaskListAPIView,
    TaskUpdateAPIView,
    TaskDestroyAPIView,
    TaskRetrieveAPIView,
    ImportantTasksListAPIView
)

app_name: str = TaskTrackerConfig.name

urlpatterns = [
    # status
    path('status/', StatusListAPIView.as_view(), name='status'),
    path('status/create/', StatusCreateAPIView.as_view(), name='status-create'),
    path('status/update/<int:pk>/', StatusUpdateAPIView.as_view(), name='status-update'),
    path('status/delete/<int:pk>/', StatusDestroyAPIView.as_view(), name='status-delete'),
    path('status/<int:pk>/', StatusRetrieveAPIView.as_view(), name='status-view'),
    # tasks
    path('', TaskListAPIView.as_view(), name='tasks'),
    path('create/', TaskCreateAPIView.as_view(), name='create_task'),
    path('update/<int:pk>/', TaskUpdateAPIView.as_view(), name='update_task'),
    path('delete/<int:pk>/', TaskDestroyAPIView.as_view(), name='delete_task'),
    path('<int:pk>/', TaskRetrieveAPIView.as_view(), name='view_task'),
    path('important/', ImportantTasksListAPIView.as_view(), name='important_tasks'),
]

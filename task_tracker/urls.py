from django.urls import path

from task_tracker.apps import TaskTrackerConfig
from task_tracker.views import (
    TaskListAPIView,
    TaskCreateAPIView,
    TaskRetrieveAPIView,
    TaskUpdateAPIView,
    TaskDestroyAPIView,
    ImportantTaskListAPIView,
    EmployeeListAPIView,
    EmployeeCreateAPIView,
    EmployeeRetrieveAPIView,
    EmployeeUpdateAPIView,
    EmployeeDestroyAPIView,
    EmployeeActiveTasksListAPIView,
)

app_name = TaskTrackerConfig.name

urlpatterns = [
    path("", TaskListAPIView.as_view(), name="task_list"),
    path("important/", ImportantTaskListAPIView.as_view(), name="important_task_list"),
    path("create/", TaskCreateAPIView.as_view(), name="task_create"),
    path("<int:pk>/", TaskRetrieveAPIView.as_view(), name="task_retrieve"),
    path("<int:pk>/update/", TaskUpdateAPIView.as_view(), name="task_update"),
    path("<int:pk>/delete/", TaskDestroyAPIView.as_view(), name="task_delete"),
    path("employee/", EmployeeListAPIView.as_view(), name="employee_list"),
    path("employee/active_tasks/", EmployeeActiveTasksListAPIView.as_view(), name="employee_active_tasks_list"),
    path("employee/create/", EmployeeCreateAPIView.as_view(), name="employee_create"),
    path("employee/<int:pk>/", EmployeeRetrieveAPIView.as_view(), name="employee_retrieve"),
    path("employee/<int:pk>/update/", EmployeeUpdateAPIView.as_view(), name="employee_update"),
    path("employee/<int:pk>/delete/", EmployeeDestroyAPIView.as_view(), name="employee_delete"),
]

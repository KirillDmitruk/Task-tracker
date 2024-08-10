from django.urls import path

from employee.apps import EmployeeConfig
from employee.views import EmployeeCreateAPIView, EmployeeListAPIView, EmployeeRetrieveAPIView, EmployeeUpdateAPIView, \
    EmployeeDestroyAPIView

app_name = EmployeeConfig.name

urlpatterns = [
    path('create/', EmployeeCreateAPIView.as_view(), name='employee_create'),
    path('', EmployeeListAPIView.as_view(), name='employee_list'),
    path('<int:pk>/', EmployeeRetrieveAPIView.as_view(), name='employee_detail'),
    path('update/<int:pk>/', EmployeeUpdateAPIView.as_view(), name='employee_update'),
    path('delete/<int:pk>/', EmployeeDestroyAPIView.as_view(), name='employee_delete'),
]

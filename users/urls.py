from django.urls import path

from users.apps import UsersConfig
from users.views import (
    PositionCreateAPIView,
    PositionListAPIView,
    PositionUpdateAPIView,
    PositionDestroyAPIView,
    PositionRetrieveAPIView,
    UserCreateAPIView,
    UserListAPIView,
    UserUpdateAPIView,
    UserDestroyAPIView,
    UserRetrieveAPIView,
    EmployedUsersListAPIView,
    AvailableUserForTaskRetrieveAPIView
)

app_name: str = UsersConfig.name

urlpatterns = [
    # positions
    path('positions/', PositionListAPIView.as_view(), name='positions'),
    path('positions/create/', PositionCreateAPIView.as_view(), name='positions-create'),
    path('positions/update/<int:pk>/', PositionUpdateAPIView.as_view(), name='positions-update'),
    path('positions/delete/<int:pk>/', PositionDestroyAPIView.as_view(), name='positions-delete'),
    path('positions/<int:pk>/', PositionRetrieveAPIView.as_view(), name='position-view'),
    # model user
    path('', UserListAPIView.as_view(), name='users'),
    path('create/', UserCreateAPIView.as_view(), name='create_user'),
    path('update/<int:pk>/', UserUpdateAPIView.as_view(), name='update_user'),
    path('delete/<int:pk>/', UserDestroyAPIView.as_view(), name='delete_user'),
    path('<int:pk>/', UserRetrieveAPIView.as_view(), name='view_user'),
    path('employed/', EmployedUsersListAPIView.as_view(), name='employed_users'),
    path('available/<int:pk>/', AvailableUserForTaskRetrieveAPIView.as_view(), name='available_users'),
]

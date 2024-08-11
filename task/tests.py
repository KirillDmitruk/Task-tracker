from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from employee.models import Employee
from task.models import Task
from users.models import User


class TestTask(APITestCase):
    """Tests for Task."""

    def setUp(self) -> None:
        self.user = User.objects.create(email="admin@example.com")
        self.client.force_authenticate(user=self.user)
        self.employee = Employee.objects.create(
            first_name="John",
            last_name="Doe",
            middle_name="Smith",
            position="Developer",
        )
        self.task = Task.objects.create(
            name="Refactoring code",
            executor=self.employee,
            deadline="2022-01-31",
        )

    def test_create_task(self):
        """Test create task"""
        url = reverse("task:task_create")
        data = {
            "name": "Implement new feature",
            "executor": self.employee.id,
            "deadline": "2022-02-28",
        }

        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_task(self):
        """Test list tasks"""
        url = reverse("task:task_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_task_by_pk(self):
        """Test get task by pk"""
        url = reverse("task:task_detail", kwargs={"pk": self.task.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_task(self):
        """Test update task"""
        url = reverse("task:task_update", kwargs={"pk": self.task.pk})
        data = {
            "name": "New task",
            "executor": self.employee.id,
            "deadline": "2023-02-28",
        }
        response = self.client.put(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_task(self):
        """Test delete task"""
        url = reverse("task:task_delete", kwargs={"pk": self.task.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from task_tracker.models import Task, Employee
from users.models import User


class TaskTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="testuser@mail.ru")
        self.employee = Employee.objects.create(
            full_name="Иванов Иван Иванович", position="инженер"
        )
        self.task = Task.objects.create(
            title="TestTask1",
            start_date="2024-09-10",
            end_date="2024-09-10",
            is_important=True,
            employee=Employee.objects.get(pk=self.employee.id),
        )

    def test_task_retrieve(self):
        url = reverse("task_tracker:task_retrieve", args=(self.task.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data["title"], self.task.title)

    def test_task_create(self):
        url = reverse("task_tracker:task_create")
        data = {
            "title": "Test2Task",
            "start_date": "2024-09-10",
            "end_date": "2024-09-10",
            "employee": self.employee.id,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.all().count(), 2)

    def test_task_update(self):
        url = reverse("task_tracker:task_update", args=(self.task.pk,))
        data = {"title": "AnotherTask"}
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data["title"], "AnotherTask")

    def test_task_destroy(self):
        url = reverse("task_tracker:task_delete", args=(self.task.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.all().count(), 0)

    def test_task_list(self):
        url = reverse("task_tracker:task_list")
        response = self.client.get(url)
        data = response.json()
        print(data)
        result = [
            {
                "id": self.task.pk,
                "term_days": 0,
                "title": "TestTask1",
                "start_date": "2024-09-10",
                "end_date": "2024-09-10",
                "status": "not_started",
                "comments": None,
                "owner": None,
                "is_active": True,
                "is_important": True,
                "parent_task": None,
                "employee": self.task.employee.id,
            }
        ]
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)
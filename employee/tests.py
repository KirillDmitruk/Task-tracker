from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from employee.models import Employee
from users.models import User


class TestEmployee(APITestCase):
    """Tests for Employee."""

    def setUp(self) -> None:
        self.user = User.objects.create(email="admin@example.com")
        self.client.force_authenticate(user=self.user)
        self.employee = Employee.objects.create(
            first_name="John",
            last_name="Doe",
            middle_name="Smith",
            position="Developer",
        )

    def test_create_employee(self):
        """Test create employee"""
        url = reverse("employee:employee_create")
        data = {
            "first_name": "Jane",
            "last_name": "Smith",
            "middle_name": "Johnson",
            "position": "QA Engineer",
        }

        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(data["first_name"], "Jane")

    def test_list_employee(self):
        """Test list employees"""
        url = reverse("employee:employee_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_employee_by_pk(self):
        """Test get employee by pk"""
        url = reverse("employee:employee_detail", kwargs={"pk": self.employee.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_employee(self):
        """Test update employee"""
        url = reverse("employee:employee_update", kwargs={"pk": self.employee.pk})
        data = {"first_name": "Kate",
                "last_name": "Williams",
                "middle_name": "Brown",
                "position": "Manager",
                }
        response = self.client.put(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_employee(self):
        """Test delete employee"""
        url = reverse("employee:employee_delete", kwargs={"pk": self.employee.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_get_busy_employees(self):
        """Test get busy employees"""
        url = reverse("employee:busy_employees")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from task_tracker.models import Status, Task
from users.models import User


class TestTaskTracker(APITestCase):
    """Test case Task Tracker"""

    def setUp(self):
        self.user = User.objects.create(email='admin@example.com')
        self.client.force_authenticate(user=self.user)
        self.status = Status.objects.create(name='В работе')
        self.task = Task.objects.create(name='Задача 1', description='Описание задачи 1', status=self.status)

    def test_create_task(self):
        """Тест создания новой задачи"""

        url = reverse('task_tracker:create_task')

        data = {
            'name': 'Задача 2',
            'description': 'Описание задачи 2',
            'status': self.status.pk,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 2)
        self.assertEqual(data.get('name'), 'Задача 2')

    def test_list_task(self):
        """Тест получения списка всех задач"""

        url = reverse('task_tracker:tasks')
        data = {
            "id": 3,
            "name": "Задача 1",
            "description": "string",
            "status": 1,
        }

        response = self.client.get(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0].get('name'), 'Задача 1')

    def test_retrieve_task(self):
        """Тест получения информации о задаче"""

        url = reverse('task_tracker:view_task', kwargs={'pk': self.task.pk})

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('name'), 'Задача 1')

    def test_update_task(self):
        """Тест изменения задачи"""

        url = reverse('task_tracker:update_task', kwargs={'pk': self.task.pk})

        data = {
            'name': 'Задача 2',
            'description': 'Описание задачи 1 updated',
            'status': self.status.pk,
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Task.objects.get(pk=self.task.pk).name, 'Задача 2')

    def test_delete_task(self):
        """Тест удаления задачи"""

        url = reverse('task_tracker:delete_task', kwargs={'pk': self.task.pk})

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)

    def test_important_tasks(self):
        """Тест получения списка важных задач"""

        url = reverse('task_tracker:important_tasks')

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)


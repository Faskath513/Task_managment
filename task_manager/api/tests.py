from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Task
from rest_framework.authtoken.models import Token
from django.urls import reverse

class TaskAPITestCase(APITestCase):
    def setUp(self):
        # Create users
        self.user1 = User.objects.create_user(username='user1', password='pass123')
        self.user2 = User.objects.create_user(username='user2', password='pass123')
        
        # Create tokens
        self.token1 = Token.objects.create(user=self.user1)
        self.token2 = Token.objects.create(user=self.user2)
        
        # Create tasks for user1
        self.task1 = Task.objects.create(title='Task 1', user=self.user1)
        self.task2 = Task.objects.create(title='Task 2', user=self.user1)
        
    def test_authentication_required(self):
        response = self.client.get(reverse('task-list'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_list_tasks(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token1.key)
        response = self.client.get(reverse('task-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
    
    def test_create_task(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token1.key)
        data = {
            'title': 'New Task',
            'description': 'Task description',
            'status': 'Pending'
        }
        response = self.client.post(reverse('task-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.filter(user=self.user1).count(), 3)
    
    def test_retrieve_task(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token1.key)
        url = reverse('task-detail', args=[self.task1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Task 1')
    
    def test_update_task(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token1.key)
        url = reverse('task-detail', args=[self.task1.id])
        data = {
            'title': 'Updated Task',
            'status': 'Completed'
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.task1.refresh_from_db()
        self.assertEqual(self.task1.title, 'Updated Task')
        self.assertEqual(self.task1.status, 'Completed')
    
    def test_delete_task(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token1.key)
        url = reverse('task-detail', args=[self.task1.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Task.objects.filter(id=self.task1.id).exists())
    
    def test_access_other_user_task(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token2.key)
        url = reverse('task-detail', args=[self.task1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

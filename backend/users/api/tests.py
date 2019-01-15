"""
Example inspiration:
https://github.com/erkarl/django-rest-framework-oauth2-provider-example/blob/master/apps/users/tests.py
"""
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from ..models import User


class CreateUserTestCase(APITestCase):
    """
    Tests if one can send a post request to create a new User

    Expected:
        Any: 201 Created
    """

    def setUp(self):
        self.data = {'username': 'testusername', 'password': 'testpassword'}

    def test_create_user(self):
        response = self.client.post(reverse('user-list'), self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ReadUserListTestCase(APITestCase):
    """
    Tests if one can get the User list with different types of authentication

    Expected:
        No authentication: 403 Forbidden
        Basic user authentication: 403 Forbidden
        Admin authentication: 200 OK
    """

    def setUp(self):
        self.superuser = User.objects.create_superuser('admin', 'admin@admin.com', 'adminpassword')
        self.user = User.objects.create_user('testuser', 'user@user.com', 'testpassword')

    def test_get_users_no_auth(self):
        response = self.client.get(reverse('user-list'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_users_regular_auth(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('user-list'))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_users_admin_auth(self):
        self.client.login(username='admin', password='adminpassword')
        response = self.client.get(reverse('user-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ReadUserDetailTestCase(APITestCase):
    """
    Tests if one can get the details of a User with different types of authentication

    Expected:
        No authentication: 403 Forbidden
        Different user authentication: 403 Forbidden
        Same user being request authentication: 200 OK
        Admin authentication: 200 OK
    """

    def setUp(self):
        self.superuser = User.objects.create_superuser('admin', 'admin@admin.com', 'adminpassword')
        self.user1 = User.objects.create_user('testuser1', 'user1@user.com', 'testpassword1')
        self.user2 = User.objects.create_user('testuser2', 'user2@user.com', 'testpassword2')

    def test_get_user_no_auth(self):
        self.client.logout()
        response = self.client.get(reverse('user-detail', kwargs={'pk': self.superuser.pk}))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_user_different_auth(self):
        self.client.login(username='testuser1', password='testpassword1')
        response = self.client.get(reverse('user-detail', kwargs={'pk': self.superuser.pk}))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_user_same_auth(self):
        self.client.login(username='testuser1', password='testpassword1')
        response = self.client.get(reverse('user-detail', kwargs={'pk': self.user1.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_user_admin_auth(self):
        self.client.login(username='admin', password='adminpassword')
        response = self.client.get(reverse('user-detail', kwargs={'pk': self.user1.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdateUserTestCase(APITestCase):
    """
    Tests if one can update a User with different types of authentication

    Expected:
        No authentication: 403 Forbidden
        Different user authentication: 403 Forbidden
        Same user being request authentication: 200 OK
        Admin authentication: 200 OK
    """

    def setUp(self):
        self.superuser = User.objects.create_superuser('admin', 'admin@admin.com', 'adminpassword')
        self.user1 = User.objects.create_user('testuser1', 'user1@user.com', 'testpassword1')
        self.user2 = User.objects.create_user('testuser2', 'user2@user.com', 'testpassword2')
        self.data = {'username': 'someusername'}

    def test_put_user_no_auth(self):
        self.client.logout()
        response = self.client.put(reverse('user-detail', kwargs={'pk': self.user1.pk}), data=self.data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_put_user_different_auth(self):
        self.client.login(username='testuser2', password='testpassword2')
        response = self.client.put(reverse('user-detail', kwargs={'pk': self.user1.pk}), data=self.data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_put_user_same_auth(self):
        self.client.login(username='testuser1', password='testpassword1')
        response = self.client.put(reverse('user-detail', kwargs={'pk': self.user1.pk}), data=self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put_user_admin_auth(self):
        self.client.login(username='admin', password='adminpassword')
        response = self.client.put(reverse('user-detail', kwargs={'pk': self.user1.pk}), data=self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteUserTestCase(APITestCase):
    """
    Tests if one can delete a User with different types of authentication

    Expected:
        No authentication: 403 Forbidden
        Different user authentication: 403 Forbidden
        Same user being request authentication: 403 Forbidden
        Admin authentication: 204 No content
    """

    def setUp(self):
        self.superuser = User.objects.create_superuser('admin', 'admin@admin.com', 'adminpassword')
        self.user1 = User.objects.create_user('testuser1', 'user1@user.com', 'testpassword1')
        self.user2 = User.objects.create_user('testuser2', 'user2@user.com', 'testpassword2')

    def test_destroy_user_no_auth(self):
        self.client.logout()
        response = self.client.delete(reverse('user-detail', kwargs={'pk': self.user1.pk}))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_destroy_user_different_auth(self):
        self.client.login(username='testuser2', password='testpassword2')
        response = self.client.delete(reverse('user-detail', kwargs={'pk': self.user1.pk}))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_destroy_user_same_auth(self):
        self.client.login(username='testuser1', password='testpassword1')
        response = self.client.delete(reverse('user-detail', kwargs={'pk': self.user1.pk}))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_destroy_user_admin_auth(self):
        self.client.login(username='admin', password='adminpassword')
        response = self.client.delete(reverse('user-detail', kwargs={'pk': self.user1.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

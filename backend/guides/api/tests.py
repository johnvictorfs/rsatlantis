from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from guides.models import Guide
from users.models import User


class CreateGuideTestCase(APITestCase):
    """
    Tests if a User can create a guide or not with different types of authentication

    Expected:
        No authentication: 401 Unauthorized
        Authenticated, but inactive: 401 Unauthorized
        Authenticated and active: 201 Created
    """

    def setUp(self):
        self.active_user = User.objects.create_user('activeuser', 'active@user.com', 'activepassword')
        self.inactive_user = User.objects.create_user('inactiveuser', 'inactive@user.com', 'inactivepassword')
        self.guide_data = {
            'title': 'Test Title',
            'description': 'Test Description',
            'content': 'Test Content',
            'category': 'pvm',
        }
        self.inactive_user.is_active = False
        self.inactive_user.save()

    def test_create_guide_no_auth(self):
        self.client.logout()
        response = self.client.post(reverse('guide-list'), data=self.guide_data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_guide_active_auth(self):
        self.client.login(username='activeuser', password='activepassword')
        response = self.client.post(reverse('guide-list'), data=self.guide_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_guide_inactive_auth(self):
        self.client.login(username='inactiveuser', password='inactivepassword')
        response = self.client.post(reverse('guide-list'), data=self.guide_data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class ReadGuideListTestCase(APITestCase):
    """
    Tests if a User can get the Guide list with different types of authentication

    Expected:
        Any: 200 OK
    """

    def setUp(self):
        self.user = User.objects.create_user('testusername', 'test@email.com', 'testpassword')

    def test_get_guides_no_auth(self):
        self.client.logout()
        response = self.client.get(reverse('guide-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_guides_auth(self):
        self.client.login(username='testusername', password='testpassword')
        response = self.client.get(reverse('guide-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ReadGuideDetailTestCase(APITestCase):
    """
    Tests if a User can get the details of a Guide with different types of authentication

    Expected:
        Any: 200 OK
    """

    def setUp(self):
        self.guide_data = {
            'title': 'Test Title',
            'description': 'Test Description',
            'content': 'Test Content',
            'category': 'pvm',
        }
        self.user = User.objects.create_user('testusername', 'test@email.com', 'testpassword')
        self.guide = Guide.objects.create(
            author=self.user,
            title=self.guide_data.get('title'),
            description=self.guide_data.get('description'),
            content=self.guide_data.get('content'),
            category=self.guide_data.get('category')
        )

    def test_get_guide_no_auth(self):
        self.client.logout()
        url = reverse('guide-detail', kwargs={'slug': self.guide.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('title'), self.guide_data.get('title'))

    def test_get_guides_auth(self):
        self.client.login(username='testusername', password='testpassword')
        url = reverse('guide-detail', kwargs={'slug': self.guide.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('title'), self.guide_data.get('title'))


class UpdateGuideTestCase(APITestCase):
    """
    Tests if a User can update a Guide with different types of authentication

    Expected:
        Not Authenticated: 401 Unauthorized
        Authenticated, but not author or admin: 403 Forbidden
        Authenticated and author: 200 OK
        Authenticated and admin: 200 OK
    """

    def setUp(self):
        self.guide_data = {
            'title': 'Test Title',
            'description': 'Test Description',
            'content': 'Test Content',
            'category': 'pvm',
        }
        self.new_guide_data = {'title': 'Updated Title'}
        self.author_user = User.objects.create_user('testusername', 'test@email.com', 'testpassword')
        self.not_author_user = User.objects.create_user('testusername2', 'test2@email.com', 'testpassword2')
        self.superuser = User.objects.create_superuser('admin', 'admin@admin.com', 'adminpassword')
        self.guide = Guide.objects.create(
            author=self.author_user,
            title=self.guide_data.get('title'),
            description=self.guide_data.get('description'),
            content=self.guide_data.get('content'),
            category=self.guide_data.get('category')
        )

    def test_update_guide_no_auth(self):
        self.client.logout()
        url = reverse('guide-detail', kwargs={'slug': self.guide.slug})
        response = self.client.patch(url, data=self.new_guide_data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertNotEqual(response.data.get('title'), self.new_guide_data.get('title'))

    def test_update_guide_not_author_auth(self):
        self.client.login(username='testusername2', password='testpassword2')
        url = reverse('guide-detail', kwargs={'slug': self.guide.slug})
        response = self.client.patch(url, data=self.new_guide_data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertNotEqual(response.data.get('title'), self.new_guide_data.get('title'))

    def test_update_guide_author_auth(self):
        self.client.login(username='testusername', password='testpassword')
        url = reverse('guide-detail', kwargs={'slug': self.guide.slug})
        response = self.client.patch(url, data=self.new_guide_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('title'), self.new_guide_data.get('title'))

    def test_update_guide_admin_auth(self):
        self.client.login(username='admin', password='adminpassword')
        new_guide_data_admin = {'title': 'Updated Title by Admin'}
        url = reverse('guide-detail', kwargs={'slug': self.guide.slug})
        response = self.client.patch(url, data=new_guide_data_admin)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('title'), new_guide_data_admin.get('title'))


class DeleteGuideTestCase(APITestCase):
    """
    Tests if a User can delete a Guide with different types of authentication

    Expected:
        Not Authenticated: 403 Forbidden
        Authenticated, but not author or admin: 403 Forbidden
        Authenticated and author: 200 OK
        Authenticated and admin: 200 OK
    """

    def setUp(self):
        self.guide_data = {
            'title': 'Test Title',
            'description': 'Test Description',
            'content': 'Test Content',
            'category': 'pvm',
        }
        self.new_guide_data = {'title': 'Updated Title'}
        self.author_user = User.objects.create_user('testusername', 'test@email.com', 'testpassword')
        self.not_author_user = User.objects.create_user('testusername2', 'test2@email.com', 'testpassword2')
        self.superuser = User.objects.create_superuser('admin', 'admin@admin.com', 'adminpassword')
        self.guide = Guide.objects.create(
            author=self.author_user,
            title=self.guide_data.get('title'),
            description=self.guide_data.get('description'),
            content=self.guide_data.get('content'),
            category=self.guide_data.get('category')
        )

    def test_destroy_guide_no_auth(self):
        self.client.logout()
        url = reverse('guide-detail', kwargs={'slug': self.guide.slug})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_destroy_guide_not_author_auth(self):
        self.client.login(username='testusername2', password='testpassword2')
        url = reverse('guide-detail', kwargs={'slug': self.guide.slug})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_destroy_guide_author_auth(self):
        self.client.login(username='testusername', password='testpassword')
        url = reverse('guide-detail', kwargs={'slug': self.guide.slug})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_destroy_guide_admin_auth(self):
        self.client.login(username='admin', password='adminpassword')
        url = reverse('guide-detail', kwargs={'slug': self.guide.slug})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class ApproveGuideTestCase(APITestCase):
    """
    Tests if a User can change the 'approved' field of a Guide with different types of authentication

    Expected:
        Not Authenticated: 403 Forbidden
        Authenticated, but not author or admin: 403 Forbidden
        Authenticated and author: 200 OK but 'approved' field is unchanged, only other fields can be updated
        Authenticated and admin: 200 OK
    """

    def setUp(self):
        self.guide_data = {
            'title': 'Test Title',
            'description': 'Test Description',
            'content': 'Test Content',
            'category': 'pvm',
        }
        self.new_guide_data = {'approved': True}
        self.author_user = User.objects.create_user('testusername', 'test@email.com', 'testpassword')
        self.not_author_user = User.objects.create_user('testusername2', 'test2@email.com', 'testpassword2')
        self.superuser = User.objects.create_superuser('admin', 'admin@admin.com', 'adminpassword')
        self.guide = Guide.objects.create(
            author=self.author_user,
            title=self.guide_data.get('title'),
            description=self.guide_data.get('description'),
            content=self.guide_data.get('content'),
            category=self.guide_data.get('category')
        )

    def test_approve_guide_no_auth(self):
        self.client.logout()
        response = self.client.post(reverse('guide-approve', kwargs={'slug': self.guide.slug}))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        guide = Guide.objects.get(pk=self.guide.pk)
        self.assertFalse(guide.approved)

    def test_approve_guide_not_author_auth(self):
        self.client.login(username='testusername2', password='testpassword2')
        response = self.client.post(reverse('guide-approve', kwargs={'slug': self.guide.slug}))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        guide = Guide.objects.get(pk=self.guide.pk)
        self.assertFalse(guide.approved)

    def test_approve_guide_author_auth(self):
        self.client.login(username='testusername', password='testpassword')
        response = self.client.post(reverse('guide-approve', kwargs={'slug': self.guide.slug}))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        guide = Guide.objects.get(pk=self.guide.pk)
        self.assertFalse(guide.approved)

    def test_approve_guide_admin_auth(self):
        self.client.login(username='admin', password='adminpassword')
        response = self.client.post(reverse('guide-approve', kwargs={'slug': self.guide.slug}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        guide = Guide.objects.get(pk=self.guide.pk)
        self.assertTrue(guide.approved)

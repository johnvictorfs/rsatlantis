from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from runescape.models import ClanMember

User = get_user_model()


class CreateClanMemberTestCase(APITestCase):
    """
    Tests if a User can add a Clan Member or not with different types of authentication

    Expected:
        Not Authenticated: 401 Unauthorized
        Authenticated: 403 Forbidden
        Authenticated and Admin: 403 Forbidden
    """

    def setUp(self):
        self.user = User.objects.create_user('user', 'test@user.com', 'password')
        self.superuser = User.objects.create_superuser('superuser', 'super@user.com', 'password')
        self.data = {
            'name': 'NRiver',
            'exp': 50_000_000,
            'rank': 'Overseer'
        }

    def test_add_member_no_auth(self):
        self.client.logout()
        response = self.client.post(reverse('clanmember-list'), data=self.data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_add_member_auth(self):
        self.client.login(username='user', password='password')
        response = self.client.post(reverse('clanmember-list'), data=self.data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_add_member_superuser(self):
        self.client.login(username='superuser', password='password')
        response = self.client.post(reverse('clanmember-list'), data=self.data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class ReadClanMemberListTestCase(APITestCase):
    """
    Tests if a User can get a list of Clan Members with different types of authentication

    Expected:
        Any: 200 OK
    """

    def setUp(self):
        self.user = User.objects.create_user('user', 'test@user.com', 'password')
        self.superuser = User.objects.create_superuser('superuser', 'super@user.com', 'password')

    def test_get_member_list_no_auth(self):
        self.client.logout()
        response = self.client.get(reverse('clanmember-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_member_list_auth(self):
        self.client.login(username='user', password='password')
        response = self.client.get(reverse('clanmember-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_member_list_superuser(self):
        self.client.login(username='superuser', password='password')
        response = self.client.get(reverse('clanmember-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ReadClanMemberDetailTestCase(APITestCase):
    """
    Tests if a User can get the details of a Clan Members with different types of authentication

    Expected:
        Any: 200 OK
    """

    def setUp(self):
        self.user = User.objects.create_user('user', 'test@user.com', 'password')
        self.superuser = User.objects.create_superuser('superuser', 'super@user.com', 'password')
        self.details = {
            'name': 'NRiver',
            'exp': 50_000_000,
            'rank': 'Overseer'
        }
        self.member = ClanMember.objects.create(
            name=self.details['name'],
            exp=self.details['exp'],
            rank=self.details['rank']
        )

    def test_get_member_list_no_auth(self):
        self.client.logout()
        response = self.client.get(reverse('clanmember-detail', kwargs={'name': self.details['name']}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.details['name'])

    def test_get_member_detail_auth(self):
        self.client.login(username='user', password='password')
        response = self.client.get(reverse('clanmember-detail', kwargs={'name': self.details['name']}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.details['name'])

    def test_get_member_detail_superuser(self):
        self.client.login(username='superuser', password='password')
        response = self.client.get(reverse('clanmember-detail', kwargs={'name': self.details['name']}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.details['name'])


class UpdateClanMemberTestCase(APITestCase):
    """
    Tests if a User can update a Clan Member with different types of authentication

    Expected:
        Not Authenticated: 401 Unauthorized
        Authenticated: 403 Forbidden
        Authenticated and Admin: 403 Forbidden
    """

    def setUp(self):
        self.user = User.objects.create_user('user', 'test@user.com', 'password')
        self.superuser = User.objects.create_superuser('superuser', 'super@user.com', 'password')
        self.details = {
            'name': 'New Name',
            'exp': 23,
            'rank': 'Admin'
        }
        self.member = ClanMember.objects.create(
            name='NRiver',
            exp=50_000_000,
            rank='Overseer'
        )

    def test_update_member_no_auth(self):
        self.client.logout()
        response = self.client.patch(reverse('clanmember-detail', kwargs={'name': 'NRiver'}), self.details)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_member_auth(self):
        self.client.login(username='user', password='password')
        response = self.client.patch(reverse('clanmember-detail', kwargs={'name': 'NRiver'}), self.details)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_member_superuser(self):
        self.client.login(username='superuser', password='password')
        response = self.client.patch(reverse('clanmember-detail', kwargs={'name': 'NRiver'}), self.details)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class DeleteClanMemberTestCase(APITestCase):
    """
    Tests if a User can delete a Clan Member with different types of authentication

    Expected:
        Not Authenticated: 401 Unauthorized
        Authenticated: 403 Forbidden
        Authenticated and Admin: 403 Forbidden
    """

    def setUp(self):
        self.user = User.objects.create_user('user', 'test@user.com', 'password')
        self.superuser = User.objects.create_superuser('superuser', 'super@user.com', 'password')
        self.member = ClanMember.objects.create(
            name='NRiver',
            exp=50_000_000,
            rank='Overseer'
        )

    def test_update_member_no_auth(self):
        self.client.logout()
        response = self.client.delete(reverse('clanmember-detail', kwargs={'name': 'NRiver'}))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_member_auth(self):
        self.client.login(username='user', password='password')
        response = self.client.delete(reverse('clanmember-detail', kwargs={'name': 'NRiver'}))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_member_superuser(self):
        self.client.login(username='superuser', password='password')
        response = self.client.delete(reverse('clanmember-detail', kwargs={'name': 'NRiver'}))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

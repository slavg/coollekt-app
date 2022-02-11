from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.db.models import Q

from coollekt.tests.utils import get_api_client
from coollekt.tests.factories.users import UserFactory
from coollekt.models.users import User


class UserTests(APITestCase):
    def setUp(self):
        UserFactory.create_batch(5)
        self.api_client = get_api_client()

    def test_list_users(self):
        url = reverse("user-list")
        response = self.api_client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEquals(len(response.data.get("results")), 6)

    def test_get_user(self):
        pk = User.objects.filter(username="admin").get().pk
        url = reverse("user-detail", kwargs={"pk": pk})
        response = self.api_client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.data.get("email"), "admin@test.com")

    def test_create_user(self):
        url = reverse("user-list")
        data = {"username": "user123", "email": "user123@test.com"}
        response = self.api_client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            User.objects.filter(username="user123").get().email, "user123@test.com"
        )

    def test_delete_user(self):
        count_before = User.objects.count()
        pk = User.objects.filter(~Q(username="admin")).first().pk
        url = reverse("user-detail", kwargs={"pk": pk})
        response = self.api_client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertGreater(count_before, User.objects.count())

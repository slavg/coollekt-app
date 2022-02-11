from coollekt.models.users import User
from rest_framework.test import APIClient

from coollekt.tests.factories.users import UserFactory


def create_user():
    UserFactory.create(username="admin", email="admin@test.com")


def get_api_client():
    create_user()
    user = User.objects.get(username="admin")
    client = APIClient(enforce_csrf_checks=True)
    client.force_authenticate(user=user)
    return client

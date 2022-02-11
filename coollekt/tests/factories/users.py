import factory

from coollekt.models.users import User
from django.utils import timezone
from faker import Faker

fake = Faker("es_ES")


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("user_name")
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    email = factory.Faker("email")
    is_staff = False
    is_active = True
    date_joined = timezone.now()
    bio = factory.Faker("text")
    birth_date = fake.date_of_birth()
    phone = factory.Faker("phone_number")

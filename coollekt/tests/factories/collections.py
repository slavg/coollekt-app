import factory

from faker import Faker

from models.collections import Category, Collection, Item
from tests.factories.fakers import category_provider

fake = Faker()
fake.add_provider(category_provider)


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = fake.category()
    description = factory.Faker("text")
    key = factory.Faker("word")


class CollectionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Collection

    name = factory.Faker("word")
    description = factory.Faker("text")
    public = True


class ItemFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Item

    name = factory.Faker("word")
    description = factory.Faker("text")
    price = factory.Faker("pricetag")

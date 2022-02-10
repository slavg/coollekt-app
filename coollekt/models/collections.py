from django.db import models

from coollekt.models.commons import AbstractModel
from coollekt.models.users import User


class Category(AbstractModel):
    name = models.CharField(max_length=1024, blank=True, null=True)
    description = models.TextField(max_length=500, blank=True, null=True)


class Collection(AbstractModel):
    name = models.CharField(max_length=1024, blank=True, null=True)
    description = models.TextField(max_length=500, blank=True, null=True)
    public = models.BooleanField(default=False)
    categories = models.ManyToManyField(Category)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Item(AbstractModel):
    name = models.CharField(max_length=1024, blank=True, null=True)
    description = models.TextField(max_length=500, blank=True, null=True)
    collection = models.ForeignKey(Collection, related_name='items', on_delete=models.CASCADE)
    price = models.DecimalField(default=0.00, decimal_places=3, max_digits=50, blank=True, null=True)





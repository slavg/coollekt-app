from django.db import models

from rest_framework import serializers

from coollekt.models.users import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups', 'bio']

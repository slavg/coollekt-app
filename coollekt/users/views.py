from django.shortcuts import render
from rest_framework import viewsets, permissions

from coollekt.models.users import User
from coollekt.users.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        return super(UserViewSet, self).list(request, *args, **kwargs)

    def create(self, request,  *args, **kwargs):
        return super(UserViewSet, self).create(request, *args, **kwargs)

    def retrieve(self, request, pk=None, *args, **kwargs):
        return super(UserViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass

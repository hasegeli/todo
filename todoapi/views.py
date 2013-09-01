from rest_framework import viewsets

from django.contrib.auth.models import User
from todoapi.models import Todo
from todoapi.serializers import UserSerializer, TodoSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TodoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


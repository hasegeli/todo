from rest_framework import viewsets

from django.contrib.auth.models import User
from todoapi.models import Todo
from todoapi.serializers import UserSerializer, TodoSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()

class TodoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows todo list of the current user to be viewed or edited.
    """
    serializer_class = TodoSerializer
    model = Todo

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)

    def pre_save(self, todo):
        todo.user = self.request.user


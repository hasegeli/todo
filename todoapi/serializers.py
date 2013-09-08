from rest_framework import serializers

from django.contrib.auth.models import User
from todoapi.models import Priority, Todo

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')

class PriorityField(serializers.RelatedField):
    def from_native(self, data):
        return Priority.objects.get(name=data)

class TodoSerializer(serializers.ModelSerializer):
    priority = PriorityField(read_only=False)

    class Meta:
        model = Todo
        fields = ('id', 'title', 'completed', 'createdAt', 'dueTo', 'priority')


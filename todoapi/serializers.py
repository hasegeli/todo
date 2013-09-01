from rest_framework import serializers

from django.contrib.auth.models import User
from todoapi.models import Priority, Todo

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email')

class PriorityField(serializers.RelatedField):
    def from_native(self, data):
        return Priority.objects.get(name=data)

class TodoSerializer(serializers.HyperlinkedModelSerializer):
    priority = PriorityField(read_only=False)

    class Meta:
        model = Todo
        fields = ('url', 'title', 'completed', 'dueTo', 'priority')


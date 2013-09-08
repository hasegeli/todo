from rest_framework import views, viewsets, filters, permissions, decorators, response, status

from django.contrib.auth.models import User
from todoapi.models import Todo
from todoapi.serializers import UserSerializer, TodoSerializer

@decorators.api_view(['POST'])
def register(request):
    serialized = UserSerializer(data=request.DATA)
    if serialized.is_valid():
        User.objects.create_user(
            serialized.init_data['username'],
            serialized.init_data['email'],
            serialized.init_data['password']
        )
        return response.Response(serialized.data, status=status.HTTP_201_CREATED)
    else:
        return response.Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)

class TodoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows todo list of the current user to be viewed or edited.
    """
    serializer_class = TodoSerializer
    model = Todo
    filter_backends = filters.OrderingFilter,
    permission_classes = permissions.IsAuthenticated,

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)

    def pre_save(self, todo):
        todo.user = self.request.user


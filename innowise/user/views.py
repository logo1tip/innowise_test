from cgitb import lookup
from user.models import CustomUser
from user.serializers import UserSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from drf_spectacular.utils import extend_schema
from task.permissions import IsSupport, IsUser



@extend_schema(description='For Support and Admin')
class UserList(generics.ListCreateAPIView):
    
    """ Представление для получения списка пользователей """
    
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSupport | IsAdminUser)



@extend_schema(description='For all')
class UserDetail(generics.RetrieveUpdateDestroyAPIView):

    """ Представление для создания, обновления и удаления пользователя """

    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSupport | IsUser | IsAdminUser)
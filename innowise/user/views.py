from user.models import CustomUser
from user.serializers import UserSerializer
from rest_framework import generics
from drf_spectacular.utils import extend_schema



@extend_schema(description='For Support and Admin')
class UserList(generics.ListCreateAPIView):
    
    """ Представление для получения списка пользователей """
    
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer



@extend_schema(description='For all')
class UserDetail(generics.RetrieveUpdateDestroyAPIView):

    """ Представление для создания, обновления и удаления пользователя """

    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
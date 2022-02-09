from task.models import Post, Comment
from task.serializers import PostSerializer, CommentSerializer
from rest_framework.permissions import IsAdminUser
from drf_spectacular.utils import extend_schema
from rest_framework import generics
from .permissions import IsSupport, IsUser


@extend_schema(description='For all')
class PostList(generics.ListCreateAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsSupport | IsAdminUser)


@extend_schema(description='For Support and Admin')
class PostUpdate(generics.RetrieveUpdateAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsSupport | IsUser | IsAdminUser)


@extend_schema(description='For all')
class PostDestroy(generics.DestroyAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsSupport | IsAdminUser)


@extend_schema(description='For all')
class CommentDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsSupport | IsUser | IsAdminUser)

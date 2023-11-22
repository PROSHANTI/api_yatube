from django.shortcuts import get_object_or_404
from rest_framework import filters, permissions, viewsets, mixins
from rest_framework.pagination import LimitOffsetPagination

from .permissions import IsAuthorOrReadOnly
from posts.models import Group, Post
from .serializers import (CommentSerializer, FollowSerializer, GroupSerializer,
                          PostSerializer)


class PostViewSet(viewsets.ModelViewSet):
    """ViewSet для CRUD операций с постами.
    Доступно только авторизованному пользователю.
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """ViewSet для CRUD операций с комментариями.
    Доступно только авторизованному пользователю,
    редактировать можно только свои комментарии.
    """

    serializer_class = CommentSerializer
    permission_classes = (IsAuthorOrReadOnly,)

    def get_post(self):
        return get_object_or_404(Post, pk=self.kwargs.get('post_id'))

    def get_queryset(self):
        post = self.get_post()
        return post.comments.all()

    def perform_create(self, serializer):
        post = self.get_post()
        serializer.save(author=self.request.user,
                        post=post)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet для отображения групп, только чтение."""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class FollowViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    """ViewSet для подписки.
    Доступно только автору или в режиме чтения
    """

    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated,
                          IsAuthorOrReadOnly)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        return self.request.user.follower.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

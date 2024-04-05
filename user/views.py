from rest_framework import viewsets, permissions
from rest_framework.response import Response

from post.models import Post, Comment
from post.serializers import PostListSerializer, CommentListSerializer
from .models import *
from .serializers import *

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


    def get_serializer_class(self):
        if self.action == 'list':
            return ProfileListSerializer
        elif self.action == 'create':
            return ProfileListSerializer
        elif self.action == 'retrieve' or self.action == 'update':
            return ProfileDetailSerializer
        return ProfileListSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentListSerializer


class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer


class BadgeViewSet(viewsets.ModelViewSet):
    queryset = UserBadge.objects.all()
    serializer_class = UserBadgeSerializer

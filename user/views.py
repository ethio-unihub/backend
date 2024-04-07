from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response

from post.models import Post, Comment
from post.views import PostViewSet as BasePostViewset, CommentListView as BaseCommentListView
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
    
class MyProfileViewSet(generics.RetrieveAPIView):
    serializer_class = ProfileDetailSerializer
    
    def retrieve(self, request, *args, **kwargs):
        user_pk = self.kwargs.get('user_pk')
        profile = get_object_or_404(Profile.objects.select_related('user'), user=user_pk)
        if request.user.is_authenticated and request.user.profile == profile:
            serializer = self.get_serializer(profile)
            return Response(serializer.data)
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class PostViewSet(BasePostViewset):
    def get_queryset(self):
        profile_pk = self.kwargs.get('profile_pk')
        queryset = Post.objects.prefetch_related('downvote','upvote','saves','images','comments').select_related('owner').filter(owner=profile_pk)
        return queryset


class CommentViewSet(BaseCommentListView):
    def get_queryset(self):
        post_pk = self.kwargs.get('profile_pk')
        queryset = Comment.objects.prefetch_related('replies').filter(post_id=post_pk, parent_comment=None)
        return queryset


class NotificationViewSet(viewsets.ModelViewSet):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        profile_pk = self.kwargs.get('profile_pk')
        queryset = Notification.objects.filter(user_profile=profile_pk)
        return queryset


class BadgeViewSet(viewsets.ModelViewSet):
    serializer_class = UserBadgeSerializer

    def get_queryset(self):
        profile_pk = self.kwargs.get('profile_pk')
        queryset = UserBadge.objects.filter(user=profile_pk)
        return queryset

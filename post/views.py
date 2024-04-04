from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import status, permissions, viewsets
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Post, Comment, PostImage
from .filter import PostFilter
from .serializers import *


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.prefetch_related('downvote','upvote','saves','images','comments').select_related('owner').all()
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = PostFilter
    search_fields = ['name','description','owner__user__first_name','owner__user__last_name']
    ordering_fields = ['upvote','added_time']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.action == 'list':
            return PostListSerializer
        elif self.action == 'create':
            return PostCreationSerializer
        elif self.action == 'update':
            instance = self.get_object()
            if instance.owner == self.request.user.profile:
                return PostUpdateSerializer
            else:
                return PostChangeSerializer
        return PostListSerializer
        
    def destroy(self, request, *args, **kwargs):
        me = request.user.profile
        instance = self.get_object()
        if instance.owner == me:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


class PostImageViewSet(viewsets.ModelViewSet):
    serializer_class = PostImageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        post_id = self.kwargs.get('post_pk')
        return PostImage.objects.filter(post=post_id)
    
    def create(self, request, *args, **kwargs):
        post_id = kwargs.get('post_pk')
        if request.user.is_authenticated and request.user.profile == Post.objects.get(id=post_id).owner:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    
    def update(self, request, *args, **kwargs):
        post_id = kwargs.get('post_pk')
        if request.user.is_authenticated and request.user.profile == Post.objects.get(id=post_id).owner:
            partial = kwargs.pop('partial', False)
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)

            if getattr(instance, '_prefetched_objects_cache', None):
                instance._prefetched_objects_cache = {}

            return Response(serializer.data)
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    
    def destroy(self, request, *args, **kwargs):
        me = request.user.profile
        instance = self.get_object()
        if instance.post.owner == me:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        post_id = self.kwargs.get('post_pk')
        queryset = Comment.objects.filter(post_id=post_id, parent_comment=None )
        return queryset
    
    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        data['author'] = request.user.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data)


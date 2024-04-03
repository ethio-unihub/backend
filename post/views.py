from django.contrib.contenttypes.models import ContentType

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user.profile)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.owner == request.user.profile:
            return super().update(request, *args, **kwargs)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        content_type = ContentType.objects.get_for_model(Post)
        serializer.save(person=self.request.user.profile, content_type=content_type)

    def get_queryset(self):
        content_type = ContentType.objects.get_for_model(Post)
        return Comment.objects.filter(content_type=content_type, object_id=self.kwargs['post_pk'])




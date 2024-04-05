from django.shortcuts import render

from rest_framework import viewsets, permissions

from .models import File
from .serializers import *


class FileListView(viewsets.ModelViewSet):
    queryset = File.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.action == 'list':
            return FileListSerializer
        elif self.action == 'create':
            return FileCreateSerializer
        elif self.action == 'update':
            instance = self.get_object()
            if instance.author == self.request.user.profile:
                return FileCreateSerializer
            return FileUpdateSerializer
        return FileListSerializer
        
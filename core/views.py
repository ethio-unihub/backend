from rest_framework import viewsets, generics, response, status

from .models import  Hashtag
from .serializers import *


class HashtagViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Hashtag.objects.prefetch_related('tags','organization','subscribers').all()
    serializer_class = HashtagSerializer


class ReportCreateAPIView(generics.CreateAPIView):
    serializer_class = ReportSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save() 
        return response.Response(serializer.data, status=status.HTTP_201_CREATED)
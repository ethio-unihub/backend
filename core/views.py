from django.db.models import Count

from rest_framework import viewsets, generics, response, status

from .models import  Hashtag
from .serializers import *


class HashtagViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Hashtag.objects.prefetch_related('tags','organization','subscribers').annotate(num_authors=Count('subscribers')).order_by('-num_authors')
    serializer_class = HashtagSerializer


class ReportCreateAPIView(generics.CreateAPIView):
    serializer_class = ReportSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save() 
        return response.Response(serializer.data, status=status.HTTP_201_CREATED)
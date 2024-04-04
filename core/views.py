from rest_framework import viewsets
from .models import  Hashtag
from .serializers import *


class HashtagViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Hashtag.objects.all()
    serializer_class = HashtagSerializer
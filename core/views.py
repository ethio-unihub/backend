
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets
from .models import  Hashtag
from .serializers import *


@api_view()
def documentation(request):
    routes = {
        "register user": "auth/users/"
    }
    return Response(routes)

class HashtagsApi(viewsets.ModelViewSet):
    queryset = Hashtag.objects.all()
    serializer_class = HashtagSerializer
    http_method_names = ['get']

    def list(self, request):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)
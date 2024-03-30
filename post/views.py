from django.db.models import Q

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Post
from .serializers import PostSerializer

@api_view(['GET'])
def search_post(request):
    query = request.GET.get('q', '')
    if query:
        posts = Post.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    else:
        return Response({"error": "No query parameter provided"}, status=status.HTTP_400_BAD_REQUEST)


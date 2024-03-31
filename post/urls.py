from rest_framework_nested import routers

from django.urls import path, include
from .views import TagViewSet, PostViewSet, PostImageViewSet, CommentViewSet, ReplyViewSet


router = routers.DefaultRouter()
router.register(r'tags', TagViewSet)
router.register(r'posts', PostViewSet)
router.register(r'post-images', PostImageViewSet)


nested_router = routers.NestedSimpleRouter(router, r'posts', lookup='content_type')
nested_router.register(r'comments', CommentViewSet, basename='post-comments')
nested_router.register(r'replies', ReplyViewSet, basename='comment-replies')


urlpatterns = [
    path('', include(router.urls)),
    path('', include(nested_router.urls)),
]

from django.urls import path
from rest_framework_nested import routers
from .views import ProfileViewSet, PostViewSet, CommentViewSet

router = routers.DefaultRouter()
router.register(r'profiles', ProfileViewSet)

profile_router = routers.NestedSimpleRouter(router, r'profiles', lookup='profile')
profile_router.register(r'posts', PostViewSet, basename='profile-posts')

post_router = routers.NestedSimpleRouter(profile_router, r'posts', lookup='post')
post_router.register(r'comments', CommentViewSet, basename='post-comments')

urlpatterns = [
    *router.urls,
    *profile_router.urls,
    *post_router.urls,
]

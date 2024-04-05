from django.urls import path
from rest_framework_nested import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'profiles', ProfileViewSet)

profile_router = routers.NestedDefaultRouter(router, r'profiles', lookup='profiles')
profile_router.register(r'notifications', NotificationViewSet, basename='profile-notification')

urlpatterns = router.urls + profile_router.urls

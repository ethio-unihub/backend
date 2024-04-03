from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'hashtags', HashtagViewSet, basename='hashtags')


urlpatterns = [
    # path('',documentation),
]

urlpatterns += router.urls
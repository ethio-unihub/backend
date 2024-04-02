from django.urls import path
from .views import *

urlpatterns = [
    path('',documentation),
    path('hashtags',HashtagsApi.as_view({'get': 'list'}))
]

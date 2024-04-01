from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView
import debug_toolbar

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/',include('core.urls')),
    path('post/',include('post.urls')),
    path('', TemplateView.as_view(template_name='index.html')),

    path('auth/',include('djoser.urls')),
    path('auth/',include('djoser.urls.jwt')),
    path('__debug__/', include(debug_toolbar.urls)),
]
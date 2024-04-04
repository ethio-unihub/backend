from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

import debug_toolbar

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/',include('core.urls')),
    path('post/',include('post.urls')),
    path('', TemplateView.as_view(template_name='index.html')),

    path('auth/',include('djoser.urls')),
    path('auth/',include('djoser.urls.jwt')),
    path('__debug__/', include(debug_toolbar.urls)),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
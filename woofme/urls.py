
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('woofme_app.urls'), name="woofme_app_urls"),
    path('add_review/', include('woofme_app.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('users/', include('users.urls')),
]
static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

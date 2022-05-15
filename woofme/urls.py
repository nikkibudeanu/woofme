
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('woofme_app.urls')),
    path('add_review/', include('woofme_app.urls')),
]

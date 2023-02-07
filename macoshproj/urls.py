from django.contrib import admin
from macoshproj import settings
from django.conf.urls.static import static
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('order/', include('order.urls')),
    path('service/', include('service.urls')),
    path('expert/', include('expert.urls')),
    path('', include('category.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

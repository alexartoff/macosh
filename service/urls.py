from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import ServiceListView, ServiceDetailView

urlpatterns = [
    path('', ServiceListView.as_view(), name='service_index_page'),
    path('<slug:slug>/', ServiceDetailView.as_view(), name='service_detail_page'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

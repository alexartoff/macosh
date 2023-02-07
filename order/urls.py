from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import OrderListView

urlpatterns = [
    path('', OrderListView.as_view(), name='order_index_page'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

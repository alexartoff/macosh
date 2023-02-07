from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import CategoryListView, CategoryDetailView

urlpatterns = [
    path('', CategoryListView.as_view(), name='index_page'),
    path('<slug:slug>/', CategoryDetailView.as_view(), name='show_category'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

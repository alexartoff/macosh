from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import ExpertDetailView, ExpertListView

urlpatterns = [
    path('', ExpertListView.as_view(), name='expert_index_page'),
    path('<slug:slug>/', ExpertDetailView.as_view(), name='show_expert'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

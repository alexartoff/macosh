from django.views.generic import ListView, DetailView
from django.utils.translation import gettext_lazy as _
# from django.views.generic.edit import FormMixin

from .models import Order


class OrderListView(ListView):
    template_name = 'order/index.html'
    model = Order
    ordering = 'id'
    context_object_name = 'orders'
    extra_context = {'title': _('Order Page')}

from django.views.generic import ListView, DetailView
from django.utils.translation import gettext_lazy as _
# from django.views.generic.edit import FormMixin

from .models import Service, ServiceImages


class ServiceListView(ListView):
    template_name = 'service/index.html'
    model = Service
    ordering = 'id'
    context_object_name = 'services'
    # TODO: List depended category
    extra_context = {'title': _('Services Page')}


class ServiceDetailView(DetailView):
    template_name = 'service/detail.html'
    model = Service
    ordering = 'id'
    context_object_name = 'service'
    extra_context = {'title': _('Services Page')}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ServiceDetailView, self).get_context_data(**kwargs)
        s = self.object
        print(f">>> {s} {s.slug}")
        context['service_images'] = ServiceImages.objects.filter(service=s)
        return context

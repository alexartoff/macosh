from django.views.generic import ListView, DetailView
from django.utils.translation import gettext_lazy as _

from .models import Expert
from service.models import Service
from category.models import Category


class ExpertListView(ListView):
    template_name = 'expert/index.html'
    model = Expert
    ordering = 'id'
    context_object_name = 'experts'
    extra_context = {'title': 'Experts list'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ExpertListView, self).get_context_data(**kwargs)
        context['categories_list'] = Category.objects.all()
        context['experts_list'] = Expert.objects.all()
        return context


class ExpertDetailView(DetailView):
    template_name = 'expert/detail.html'
    model = Expert
    context_object_name = 'expert'
    extra_context = {'title': _('Expert info')}

    def get_context_data(self, **kwargs):
        context = super(ExpertDetailView, self).get_context_data(**kwargs)
        expert = Expert.objects.get(slug=self.kwargs['slug'])
        services = Service.objects.filter(expert=expert)
        context['categories_list'] = Category.objects.all()
        context['expert_title'] = expert
        context['services'] = services
        return context

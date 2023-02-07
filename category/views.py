# from django.http import Http404
# from django.shortcuts import redirect
# from django.contrib import messages
# from django.contrib.messages.views import SuccessMessageMixin
# from django.db.models import ProtectedError
# from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView
from django.utils.translation import gettext_lazy as _
# from django.views.generic.edit import FormMixin

from .models import Category


class CategoryListView(ListView):
    template_name = 'category/index.html'
    model = Category
    ordering = 'id'
    context_object_name = 'categories'
    extra_context = {'title': 'Index Page'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        categories = Category.objects.all()
        context['cat_list'] = []
        for item in categories:
            context['cat_list'].append(item)
        return context


class CategoryDetailView(DetailView):
    template_name = 'category/detail.html'
    model = Category
    context_object_name = 'category'
    extra_context = {'title': _('Category info')}

    def get_context_data(self, **kwargs):
        context = super(CategoryDetailView, self).get_context_data(**kwargs)
        category = Category.objects.get(slug=self.object.slug)
        context['category_title'] = category
        context['category_description'] = category.description
        context['experts_list'] = category.expert.all()
        return context

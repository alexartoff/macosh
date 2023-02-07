from django.db import models
from django.utils.translation import gettext_lazy as _
from expert.models import Expert


def category_image_path(instance, filename):
    return f'img/category/{instance.slug}/{filename}'


class Category(models.Model):
    name = models.CharField(
        max_length=90,
        verbose_name='Category'
    )
    slug = models.SlugField(
        max_length=90,
        unique=True,
        verbose_name='Category slug'
    )
    image = models.ImageField(
        default='img/category/default/category-default.png',
        upload_to=category_image_path,
        verbose_name=_('Category image')
    )
    description = models.CharField(
        max_length=255,
        verbose_name='Category description'
    )
    expert = models.ManyToManyField(
        Expert,
        verbose_name='Category expert\'s'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def show_experts(self):
        experts = self.expert.all()
        _ = ''
        for item in experts:
            _ += f'{item}; '
        return _[:-1]

    show_experts.short_description = _('Experts list')

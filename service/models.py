from django.db import models
from django.utils.translation import gettext_lazy as _
from category.models import Expert


# Create your models here.
def main_image_path(instance, filename):
    return f'img/service/{instance.title}/{filename}'


def additional_image_path(instance, filename):
    return f'img/service/{instance.service}/gall/{filename}'


class Service(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name=_('Service title')
    )
    slug = models.SlugField(
        max_length=255,
        unique=True,
        blank=True,
        null=True,
        verbose_name=_('Service slug')
    )
    description = models.TextField(
        default='',
        verbose_name=_('Service description')
    )
    photo = models.ImageField(
        default='img/service/default/image-default.png',
        upload_to=main_image_path,
        verbose_name=_('Service main image')
    )
    expert = models.ForeignKey(
        Expert,
        on_delete=models.CASCADE,
        verbose_name=_('Service expert')
    )
    price = models.IntegerField(
        default=0,
        verbose_name=_('Service price')
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Created')
    )
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name=_('Updated')
    )
    is_published = models.BooleanField(
        default=True,
        verbose_name=_('Published?')
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"


class ServiceImages(models.Model):
    description = models.TextField(
        default='',
        verbose_name=_('Service image description')
    )
    alt_text = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name=_('Service image alt text')
    )
    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        verbose_name=_('Service')
    )
    image = models.ImageField(
        default='img/service/default/image-default.png',
        upload_to=additional_image_path,
        verbose_name=_('Service additional image')
    )
    slug = models.SlugField(
        max_length=255,
        unique=True,
        blank=True,
        null=True,
        verbose_name=_('Service image slug')
    )
    uploaded = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Service image added')
    )
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name=_('Service image updated')
    )

    class Meta:
        verbose_name = "Service image"
        verbose_name_plural = "Service images"

    # def image_path(self):
    #     s = self.service
    #     print(f'>>> image_path={s}')
    #     return f'img/service/{s}/gall/'
    #
    # def save(self, *args, **kwargs):
    #     self.image = self.image_path
    #     self.validate_unique()
    #     super(ServiceImages, self).save(*args, **kwargs)

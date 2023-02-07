from django.db import models
from django.utils.translation import gettext_lazy as _
from service.models import Service


# Create your models here.
class Order(models.Model):
    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        verbose_name=_('Order service')
    )
    client_name = models.CharField(
        max_length=90,
        verbose_name=_('Order client name')
    )
    client_lastname = models.CharField(
        max_length=90,
        verbose_name=_('Order client lastname')
    )
    client_email = models.EmailField(
        verbose_name=_('Order client email')
    )
    comment = models.TextField(
        default='',
        verbose_name=_('Order client comment')
    )
    order_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Order created'
    )
    is_done = models.BooleanField(
        default=False,
        verbose_name=_('Completed?')
    )

    def __str__(self):
        return f'{self.client_name} {self.client_lastname}'

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"

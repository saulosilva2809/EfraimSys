from .choices import PAYMENT_METHOD_TYPE_CHOICES

from django.db import models

from apps.base.models import BaseModel


class FunctionModel(BaseModel):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    payment_type = models.CharField(max_length=50, choices=PAYMENT_METHOD_TYPE_CHOICES, default='day')
    value = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    class Meta:
        verbose_name = "Função"
        verbose_name_plural = "Funções"

    def __str__(self):
        return self.name

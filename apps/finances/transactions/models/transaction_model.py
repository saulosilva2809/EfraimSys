from .choices import TRANSACTION_MODEL_TYPE_CHOICES

from django.db import models

from apps.base.models import BaseModel
from apps.finances.accounts. models import AccountModel


class TransactionModel(BaseModel):
    account = models.ForeignKey(
        AccountModel,
        on_delete=models.SET_NULL,
        null=True,
        related_name='transactions'
    )
    value = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField(null=True, blank=True)
    proof = models.ImageField(upload_to='proof/', null=True, blank=True)
    type_transaction = models.CharField(max_length=50, choices=TRANSACTION_MODEL_TYPE_CHOICES)

    class Meta:
        verbose_name = 'Transação'
        verbose_name_plural = 'Transações'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.type_transaction} - {self.value}'

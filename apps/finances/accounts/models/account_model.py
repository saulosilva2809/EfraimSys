from .choices import (
    ACCOUNT_MODEL_CURRENCY_CHOICES,
    ACCOUNT_MODEL_BANK_CHOICES,
    ACCOUNT_MODEL_TYPE_CHOICES
)

from django.db import models

from apps.base.models import BaseModel


class AccountModel(BaseModel):
    name = models.CharField(max_length=200, help_text="Nome interno para identificar a conta (ex: Conta Principal)")
    bank = models.CharField(max_length=60, choices=ACCOUNT_MODEL_BANK_CHOICES)
    agency = models.CharField(max_length=10, help_text="Número da agência bancária")
    account_number = models.CharField(max_length=20, help_text="Número da conta bancária")
    account_type = models.CharField(max_length=20, choices=ACCOUNT_MODEL_TYPE_CHOICES)
    current_balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    currency = models.CharField(max_length=10, choices=ACCOUNT_MODEL_CURRENCY_CHOICES)  # Se um dia quiser multi-moeda
    is_active = models.BooleanField(default=True)  # se a conta ainda está em uso
    description = models.TextField(blank=True, null=True)  # info extra

    class Meta:
        verbose_name = "Conta Bancária"
        verbose_name_plural = "Contas Bancárias"

    def __str__(self):
        return f"{self.name} - {self.bank}"

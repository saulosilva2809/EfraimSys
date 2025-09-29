import django_filters

from .models import TransactionModel


class TransactionFilter(django_filters.FilterSet):
    class Meta:
        model = TransactionModel
        fields = {
            "account": ["exact"],
            "type_transaction": ["exact"],
        }

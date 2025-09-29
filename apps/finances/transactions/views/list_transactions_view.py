from apps.finances.transactions.filters import TransactionFilter

from django.views.generic import ListView
from django_filters.views import FilterView

from apps.finances.transactions.models import TransactionModel


class ListTransactionView(FilterView, ListView):
    model = TransactionModel
    template_name = 'finances/transactions/list_transactions.html'
    paginate_by = 30
    filterset_class = TransactionFilter

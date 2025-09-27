from django.views.generic import ListView

from apps.finances.transactions.models import TransactionModel


class ListTransactionView(ListView):
    model = TransactionModel
    template_name = 'finances/transactions/list_transactions.html'
    paginate_by = 30

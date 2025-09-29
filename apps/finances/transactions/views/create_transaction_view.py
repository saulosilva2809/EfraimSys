from django.contrib import messages
from django.views.generic import CreateView
from django.urls import reverse_lazy

from apps.finances.transactions.models import TransactionModel


class CreateTransactionView(CreateView):
    model = TransactionModel
    template_name = 'finances/transactions/create_transaction.html'
    fields = '__all__'
    success_url = reverse_lazy('list_transactions_view')

    def form_valid(self, form):
        messages.success(self.request, 'Transação adicionada com sucesso!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Erro ao adicionar transação, tente novamente mais tarde!')
        return super().form_invalid(form)

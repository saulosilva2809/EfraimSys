from django.contrib import messages
from django.views.generic import CreateView
from django.urls import reverse_lazy

from apps.finances.accounts.models import AccountModel


class CreateAccountView(CreateView):
    model = AccountModel
    template_name = 'finances/accounts/create_account.html'
    fields = '__all__'
    success_url = reverse_lazy('list_accounts_view')

    def form_valid(self, form):
        messages.success(self.request, 'Conta adicionada com sucesso!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Erro ao adicionar conta, tente novamente mais tarde!')
        return super().form_invalid(form)

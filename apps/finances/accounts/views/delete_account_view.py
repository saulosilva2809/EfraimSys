from django.contrib import messages
from django.views.generic import DeleteView
from django.urls import reverse_lazy

from apps.finances.accounts.models import AccountModel


class DeleteAccountView(DeleteView):
    model = AccountModel
    template_name = 'finances/accounts/delete_account.html'
    success_url = reverse_lazy('list_accounts_view')

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Conta excluída com sucesso!')
        return super().delete(request, *args, **kwargs)

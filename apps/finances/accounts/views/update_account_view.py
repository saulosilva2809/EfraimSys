from django.contrib import messages
from django.views.generic import UpdateView
from django.urls import reverse_lazy

from apps.finances.accounts.models import AccountModel


class UpdateAccountView(UpdateView):
    model = AccountModel
    template_name = 'finances/accounts/update_account.html'
    fields = '__all__'
    success_url = reverse_lazy('list_accounts_view')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = self.get_object()
        return context

    def form_valid(self, form):
        messages.success(self.request, 'Conta atualizada com sucesso!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Erro ao atualizar conta, tente novamente mais tarde!')
        return super().form_invalid(form)

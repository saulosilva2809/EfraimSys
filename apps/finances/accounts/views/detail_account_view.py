from django.views.generic import DetailView

from apps.finances.accounts.models import AccountModel


class DetailAccountView(DetailView):
    model = AccountModel
    template_name = 'finances/accounts/detail_account.html'

from django.db.models import Sum
from django.views.generic import ListView

from apps.finances.accounts.models import AccountModel


class ListAccountsView(ListView):
    model = AccountModel
    template_name = 'finances/accounts/list_accounts.html'
    paginate_by = 30
    context_object_name = 'accounts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_accounts'] = AccountModel.objects.all().count()
        context['total_balance'] = AccountModel.objects.aggregate(
            total=Sum('current_balance')
        )['total'] or 0
        context['active_accounts'] = AccountModel.objects.filter(is_active=True).count()
        context['banks_count'] = AccountModel.objects.values_list('bank', flat=True).distinct().count()

        return context

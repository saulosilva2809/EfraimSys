from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from apps.finances.accounts.models import AccountModel
from apps.finances.transactions.models import TransactionModel


class DashboardFinanceView(LoginRequiredMixin, TemplateView):
    template_name = 'base/dashboard_finance.html'
    login_url = reverse_lazy('login_view')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_balance'] = AccountModel.objects.aggregate(
            total=Sum('current_balance')
        )['total'] or 0
        context['total_recipes'] = TransactionModel.objects.filter(type_transaction='receita').aggregate(
            total=Sum('value')
        )['total'] or 0
        context['total_expenses'] = TransactionModel.objects.filter(type_transaction='despesa').aggregate(
            total=Sum('value')
        )['total'] or 0
        context['net_balance'] = context['total_recipes'] - context['total_expenses']
        context['recent_transactions'] = TransactionModel.objects.all().order_by('-created_at')

        return context

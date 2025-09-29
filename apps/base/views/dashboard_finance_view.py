from apps.base.utils import get_dashboard_context

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView


class DashboardFinanceView(LoginRequiredMixin, TemplateView):
    template_name = 'base/dashboard_finance.html'
    login_url = reverse_lazy('login_view')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_dashboard_context())

        return context

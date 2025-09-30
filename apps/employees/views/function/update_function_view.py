from django.contrib import messages
from django.views.generic import UpdateView
from django.urls import reverse_lazy

from apps.employees.models import FunctionModel


class UpdateFunctionView(UpdateView):
    model = FunctionModel
    template_name = 'employees/function/update_function.html'
    fields = ['name', 'description', 'payment_type']
    success_url = reverse_lazy('list_functions_view')

    def form_valid(self, form):
        messages.success(self.request, 'Função atualizada com sucesso!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Erro ao atualizar função, tente novamente mais tarde!')
        return super().form_invalid(form)

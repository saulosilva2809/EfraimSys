from django.contrib import messages
from django.views.generic import DeleteView
from django.urls import reverse_lazy

from apps.employees.models import FunctionModel


class DeleteFunctionView(DeleteView):
    model = FunctionModel
    template_name = 'employees/function/delete_function.html'
    success_url = reverse_lazy('list_functions_view')

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Função excluída com sucesso!')
        return super().delete(request, *args, **kwargs)

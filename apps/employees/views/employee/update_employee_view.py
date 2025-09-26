from django.contrib import messages
from django.views.generic import UpdateView
from django.urls import reverse_lazy

from apps.employees.models import EmployeeModel


class UpdateEmployeeView(UpdateView):
    model = EmployeeModel
    template_name = 'employees/employee/update_employee.html'
    fields = '__all__'
    success_url = reverse_lazy('list_employees_view')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = self.get_object()
        return context

    def form_valid(self, form):
        messages.success(self.request, 'Funcionário atualizado com sucesso!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Erro ao atualizar funcionário, tente novamente mais tarde!')
        return super().form_invalid(form)

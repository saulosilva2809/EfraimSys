from django.contrib import messages
from django.views.generic import CreateView
from django.urls import reverse_lazy

from apps.employees.models import EmployeeModel


class CreateEmployeeView(CreateView):
    model = EmployeeModel
    template_name = 'employees/employee/create_employee.html'
    fields = '__all__'
    success_url = reverse_lazy('list_employees_view')

    def form_valid(self, form):
        messages.success(self.request, 'Funcionário adicionado com sucesso!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Erro ao adicionar funcionário, tente novamente mais tarde!')
        return super().form_invalid(form)

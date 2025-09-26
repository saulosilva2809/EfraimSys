from django.contrib import messages
from django.views.generic import DeleteView
from django.urls import reverse_lazy

from apps.employees.models import EmployeeModel


class DeleteEmployeeView(DeleteView):
    model = EmployeeModel
    template_name = 'employees/employee/delete_employee.html'
    success_url = reverse_lazy('list_employees_view')

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Funcionário excluído com sucesso!')
        return super().delete(request, *args, **kwargs)

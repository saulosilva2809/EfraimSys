from django.views.generic import ListView

from apps.employees.models import EmployeeModel


class ListEmployeesView(ListView):
    model = EmployeeModel
    template_name = 'employees/employee/list_employees.html'
    paginate_by = 30

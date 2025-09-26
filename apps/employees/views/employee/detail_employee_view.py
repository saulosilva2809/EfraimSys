from django.views.generic import DetailView

from apps.employees.models import EmployeeModel


class DetailEmployeeView(DetailView):
    model = EmployeeModel
    template_name = 'employees/employee/detail_employee.html'

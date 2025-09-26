from django.views.generic import ListView

from apps.employees.models import FunctionModel


class ListFunctionsView(ListView):
    model = FunctionModel
    template_name = 'employees/function/list_functions.html'
    paginate_by = 30

from django.contrib import messages
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.http import JsonResponse

from apps.employees.models import FunctionModel


class CreateFunctionView(CreateView):
    model = FunctionModel
    template_name = 'employees/function/create_function.html'
    fields = ['name', 'description']
    success_url = reverse_lazy('list_functions_view')

    def form_valid(self, form):
        # Se for uma requisição AJAX, retornar JSON
        if self.request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            function = form.save()
            return JsonResponse({
                'success': True,
                'message': 'Função adicionada com sucesso!',
                'function': {
                    'id': str(function.id),
                    'name': function.name,
                    'description': function.description or ''
                }
            })
        
        # Comportamento normal para requisições não-AJAX
        messages.success(self.request, 'Função adicionada com sucesso!')
        return super().form_valid(form)

    def form_invalid(self, form):
        # Se for uma requisição AJAX, retornar JSON com erros
        if self.request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            errors = {}
            for field, field_errors in form.errors.items():
                errors[field] = [str(error) for error in field_errors]
            
            return JsonResponse({
                'success': False,
                'message': 'Erro ao adicionar função. Verifique os dados informados.',
                'errors': errors
            }, status=400)
        
        # Comportamento normal para requisições não-AJAX
        messages.error(self.request, 'Erro ao adicionar função, tente novamente mais tarde!')
        return super().form_invalid(form)

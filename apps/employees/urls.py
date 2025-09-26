from .views import (
    CreateEmployeeView,
    DeleteEmployeeView,
    DetailEmployeeView,
    ListEmployeesView,
    UpdateEmployeeView,

    CreateFunctionView,
    DeleteFunctionView,
    ListFunctionsView,
    UpdateFunctionView
)

from django.urls import path


urlpatterns = [
    path('create-employee/', view=CreateEmployeeView.as_view(), name='create_employee_view'),
    path('delete-employee/<uuid:pk>/', view=DeleteEmployeeView.as_view(), name='delete_employee_view'),
    path('detail-employee/<uuid:pk>/', view=DetailEmployeeView.as_view(), name='detail_employee_view'),
    path('list-employees/', view=ListEmployeesView.as_view(), name='list_employees_view'),
    path('update-employee/<uuid:pk>/', view=UpdateEmployeeView.as_view(), name='update_employee_view'),

    path('create-function/', view=CreateFunctionView.as_view(), name='create_function_view'),
    path('delete-function/<uuid:pk>/', view=DeleteFunctionView.as_view(), name='delete_function_view'),
    path('list-functions/', view=ListFunctionsView.as_view(), name='list_functions_view'),
    path('update-function/<uuid:pk>/', view=UpdateFunctionView.as_view(), name='update_function_view'),
]

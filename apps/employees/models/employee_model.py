from .function_model import FunctionModel

from django.db import models

from apps.base.models import BaseModel


class EmployeeModel(BaseModel):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    cpf = models.CharField(max_length=14, unique=True)
    birth_date = models.DateField(null=True, blank=True)
    photo = models.ImageField(upload_to='employees/', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    function = models.ForeignKey(FunctionModel, on_delete=models.DO_NOTHING)
    admission_date = models.DateField()
    resignation_date = models.DateField(null=True, blank=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    workload = models.IntegerField(default=40, null=True, blank=True)
    employment_type = models.CharField(
        max_length=50,
        choices=[('CLT', 'CLT'), ('At', 'Autônomo')]
    )
    obs = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Funcionário"
        verbose_name_plural = "Funcionários"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

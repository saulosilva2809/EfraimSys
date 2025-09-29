from datetime import timedelta

from django.db.models import Sum
from django.utils import timezone

from apps.finances.accounts.models import AccountModel
from apps.finances.transactions.models import TransactionModel


def calculate_percentage_variation(current, previous):
    if previous == 0:
        return 0 if current == 0 else 100  # avoid division by zero
    variation = ((current - previous) / previous) * 100
    return round(variation, 2)


def get_dashboard_context():
    today = timezone.now().date()
    first_day_current_month = today.replace(day=1)
    first_day_previous_month = (first_day_current_month - timedelta(days=1)).replace(day=1)

    context = {}

    context["total_balance"] = AccountModel.objects.aggregate(
        total=Sum("current_balance")
    )["total"] or 0

    current_revenue = TransactionModel.objects.filter(
        created_at__gte=first_day_current_month,
        type_transaction="receita"
    ).aggregate(total=Sum("value"))["total"] or 0

    previous_revenue = TransactionModel.objects.filter(
        created_at__gte=first_day_previous_month,
        created_at__lt=first_day_current_month,
        type_transaction="receita"
    ).aggregate(total=Sum("value"))["total"] or 0

    context["total_recipes"] = current_revenue
    context["recipes_variation"] = calculate_percentage_variation(current_revenue, previous_revenue)

    current_expenses = TransactionModel.objects.filter(
        created_at__gte=first_day_current_month,
        type_transaction="despesa"
    ).aggregate(total=Sum("value"))["total"] or 0

    previous_expenses = TransactionModel.objects.filter(
        created_at__gte=first_day_previous_month,
        created_at__lt=first_day_current_month,
        type_transaction="despesa"
    ).aggregate(total=Sum("value"))["total"] or 0

    context["total_expenses"] = current_expenses
    context["expenses_variation"] = calculate_percentage_variation(current_expenses, previous_expenses)

    context["net_balance"] = current_revenue - current_expenses
    context["net_balance_variation"] = calculate_percentage_variation(
        current_revenue - current_expenses,
        previous_revenue - previous_expenses
    )

    return context

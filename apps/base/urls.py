from .views import HomeView, DashboardFinanceView

from django.urls import path


urlpatterns = [
    path('', view=HomeView.as_view(), name='home_view'),
    path('dashboard-finance/', view=DashboardFinanceView.as_view(), name='dashboard_finance_view'),
]

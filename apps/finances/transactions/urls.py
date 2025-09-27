from .views import (
    CreateTransactionView,
    ListTransactionView,
)
from django.urls import path


urlpatterns = [
    path('create-transaction/', view=CreateTransactionView.as_view(), name='create_transaction_view'),
    path('list-transactions/', view=ListTransactionView.as_view(), name='list_transactions_view'),
]

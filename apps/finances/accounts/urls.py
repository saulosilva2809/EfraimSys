from .views import (
    CreateAccountView,
    DetailAccountView,
    DeleteAccountView,
    ListAccountsView,
    UpdateAccountView
)

from django.urls import path


urlpatterns = [
    path('create-account/', view=CreateAccountView.as_view(), name='create_account_view'),
    path('detail-account/<uuid:pk>/', view=DetailAccountView.as_view(), name='detail_account_view'),
    path('delete-account/<uuid:pk>/', view=DeleteAccountView.as_view(), name='delete_account_view'),
    path('list-accounts/', view=ListAccountsView.as_view(), name='list_accounts_view'),
    path('update-account/<uuid:pk>/', view=UpdateAccountView.as_view(), name='update_accounts_view'),
]

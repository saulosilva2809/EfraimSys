from .views import LoginView

from django.contrib.auth.views import LogoutView
from django.urls import path


urlpatterns = [
    path('login/', view=LoginView.as_view(), name='login_view'),
    path('logout/', LogoutView.as_view(next_page='login_view'), name='logout_view'),
]

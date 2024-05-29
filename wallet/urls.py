from django.urls import path

from . import views

urlpatterns = [
    path("wallets/", views.WalletListAPIView.as_view(), name="wallets"),
    path("transactions/", views.TransactionListAPIView.as_view(), name="transactions"),
]

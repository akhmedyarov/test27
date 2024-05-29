from rest_framework import generics
from rest_framework_json_api import filters
from rest_framework_json_api import django_filters
from rest_framework_json_api.pagination import JsonApiPageNumberPagination

from .models import Wallet, Transaction
from .serializers import WalletSerializer, TransactionSerializer


class CommonListAPiViewMixin(
    generics.ListAPIView,
    JsonApiPageNumberPagination,
):
    filter_backends = (
        filters.QueryParameterValidationFilter,
        filters.OrderingFilter,
        django_filters.DjangoFilterBackend,
    )
    ordering_fields = ["created_at", "updated_at"]


class WalletListAPIView(CommonListAPiViewMixin):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
    filterset_fields = {
        "id": ("exact",),
        "label": ("icontains", "iexact", "contains"),
    }


class TransactionListAPIView(CommonListAPiViewMixin):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    filterset_fields = {
        "id": ("exact",),
        "wallet": ("exact",),
        "txid": ("exact",),
    }

from rest_framework import serializers

from wallet.models import Wallet, Transaction


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = [
            "id",
            "label",
            "balance",
        ]


class TransactionSerializer(serializers.ModelSerializer):
    wallet = WalletSerializer()

    class Meta:
        model = Transaction
        fields = [
            "id",
            "wallet",
            "txid",
            "amount",
        ]

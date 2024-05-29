import uuid

import pytest
from ddf import G

from wallet.models import Wallet, Transaction
from wallet.exceptions import NegativeBalanceException


@pytest.mark.django_db
def test_wallet_negative_balance_error():
    wallet = G(Wallet, balance=100, label="Just label")
    G(Transaction, wallet=wallet, amount=1000, txid=str(uuid.uuid4()))

    with pytest.raises(NegativeBalanceException):
        Transaction.objects.create(wallet=wallet, amount=-2000, txid=str(uuid.uuid4()))

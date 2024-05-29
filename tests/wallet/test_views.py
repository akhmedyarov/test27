import uuid

import pytest
from random import randint

from django.urls import reverse
from rest_framework import status
from ddf import G
from wallet.models import Wallet, Transaction


@pytest.mark.django_db
def test_api_list_wallets(client):
    G(
        Wallet,
        label="Test label",
        balance=randint(0, 1000),
        n=3,
    )

    url = reverse("api:wallets")
    resp = client.get(url)

    assert resp.status_code == status.HTTP_200_OK
    assert resp.json()["meta"]["pagination"]["count"] == 3


@pytest.mark.django_db
def test_api_list_wallets_filtering(client):
    G(
        Wallet,
        label="Test label",
        balance=randint(0, 1000),
        n=3,
    )
    G(
        Wallet,
        label="Test label should find",
        balance=randint(0, 1000),
    )

    url = reverse("api:wallets")
    resp = client.get(
        url,
        {
            "filter[label.icontains]": "should find",
        },
    )

    assert resp.status_code == status.HTTP_200_OK
    assert resp.json()["meta"]["pagination"]["count"] == 1


@pytest.mark.django_db
def test_api_list_wallets_ordering(client):
    G(
        Wallet,
        label="Test label",
        balance=randint(0, 1000),
        n=3,
    )
    wallet_to_find = G(
        Wallet,
        label="Test label should be first",
        balance=randint(0, 1000),
    )

    url = reverse("api:wallets")
    resp = client.get(
        url,
        {
            "sort": "-created_at",
        },
    )
    resp_json = resp.json()

    assert resp.status_code == status.HTTP_200_OK
    assert resp_json["meta"]["pagination"]["count"] == 4
    assert resp_json["data"][0]["id"] == str(wallet_to_find.id)


@pytest.mark.django_db
def test_api_list_wallets_invalid_ordering(client):
    G(
        Wallet,
        label="Test label",
        balance=randint(0, 1000),
        n=3,
    )

    url = reverse("api:wallets")
    resp = client.get(
        url,
        {
            "sort": "label",
        },
    )

    assert resp.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_api_list_transactions(client):
    G(
        Transaction,
        amount=randint(0, 200),
        txid=str(uuid.uuid4()),
    )
    G(
        Transaction,
        amount=randint(0, 200),
        txid=str(uuid.uuid4()),
    )

    url = reverse("api:transactions")
    resp = client.get(url)

    assert resp.status_code == status.HTTP_200_OK
    assert resp.json()["meta"]["pagination"]["count"] == 2


@pytest.mark.django_db
def test_api_list_transactions_filtering(client):
    G(
        Transaction,
        amount=randint(0, 200),
        txid=str(uuid.uuid4()),
    )
    transaction_to_find = G(
        Transaction,
        amount=randint(0, 1000),
        txid=str(uuid.uuid4()),
    )

    url = reverse("api:transactions")
    resp = client.get(
        url,
        {
            "filter[wallet]": str(transaction_to_find.wallet.id),
        },
    )

    assert resp.status_code == status.HTTP_200_OK
    assert resp.json()["meta"]["pagination"]["count"] == 1


@pytest.mark.django_db
def test_api_list_transactions_ordering(client):
    G(
        Transaction,
        amount=randint(0, 200),
        txid=str(uuid.uuid4()),
    )
    wallet_to_find = G(
        Transaction,
        amount=randint(0, 1000),
        txid=str(uuid.uuid4()),
    )

    url = reverse("api:transactions")
    resp = client.get(
        url,
        {
            "sort": "-created_at",
        },
    )
    resp_json = resp.json()

    assert resp.status_code == status.HTTP_200_OK
    assert resp_json["meta"]["pagination"]["count"] == 2
    assert resp_json["data"][0]["id"] == str(wallet_to_find.id)


@pytest.mark.django_db
def test_api_list_transactions_invalid_ordering(client):
    G(
        Transaction,
        amount=randint(0, 200),
        txid=str(uuid.uuid4()),
    )

    url = reverse("api:transactions")
    resp = client.get(
        url,
        {
            "sort": "label",
        },
    )

    assert resp.status_code == status.HTTP_400_BAD_REQUEST

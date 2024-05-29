from uuid import uuid4
from django.db import models


class Wallet(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    label = models.CharField(max_length=255)
    balance = models.DecimalField(decimal_places=18, max_digits=30, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("created_at",)


class Transaction(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    txid = models.CharField(max_length=255, unique=True)
    amount = models.DecimalField(decimal_places=18, max_digits=30, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("created_at",)

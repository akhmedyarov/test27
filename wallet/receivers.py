from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from wallet.models import Transaction
from wallet.exceptions import NegativeBalanceException


@receiver(pre_save, sender=Transaction)
def check_balance(sender, instance, **kwargs):
    if instance.pk is None:
        return

    if instance.wallet.balance + instance.amount < 0:
        raise NegativeBalanceException


@receiver(post_save, sender=Transaction)
def update_balance(sender, instance, created, **kwargs):
    if not created:
        return

    wallet = instance.wallet
    wallet.balance += instance.amount

    wallet.save(update_fields=["balance"])

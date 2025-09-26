from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.finances.transactions.models import TransactionModel


@receiver(post_save, sender=TransactionModel)
def update_accounts_balance(sender, instance, created, **kwargs):
    if created:
        if instance.type_transaction == 'despesa':
            instance.account.current_balance -= instance.value
            instance.account.save()

        else:
            instance.account.current_balance += instance.value
            instance.account.save()

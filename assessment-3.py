'''By default, Django signals run in the same database transaction as the caller.
 This means if the database transaction is not committed successfully,
 the signal handler's changes will also be rolled back.'''

# signals.py
from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def user_created_handler(sender, instance, created, **kwargs):
    if created:
        print("Signal received: Saving a related object.")
        # Try to save a related object within the same transaction
        instance.profile = "Profile information"
        # Simulating an exception to cause transaction rollback
        raise Exception("Simulating a failure to see if transaction is rolled back")

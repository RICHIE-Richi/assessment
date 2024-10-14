'''By default, Django signals are executed synchronously.
This means that when a signal is sent, 
the connected receiver functions are executed immediately, 
in the same thread and process that sent the signal.'''

# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

import time

@receiver(post_save, sender=User)
def user_created_handler(sender, instance, created, **kwargs):
    if created:
        print("User created signal received.")
        # Simulate a long-running task
        time.sleep(5)
        print("Signal handling complete.")

#The user_created_handler function will be called when a new User instance is saved.
#It simulates a long-running task using time.sleep(5).

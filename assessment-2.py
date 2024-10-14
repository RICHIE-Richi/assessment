'''By default, Django signals run in the same thread as the caller. 
This means the receiver functions connected to a signal are executed immediately 
within the same thread that sends the signal.'''

# signals.py
import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def user_created_handler(sender, instance, created, **kwargs):
    if created:
        print("Signal receiver thread:", threading.current_thread().name)
        print("User created signal received.")

#------------------------------------------------------------------------


# In a Django shell or view
import threading
from django.contrib.auth.models import User

print("Main thread:", threading.current_thread().name)
User.objects.create(username='new_user')

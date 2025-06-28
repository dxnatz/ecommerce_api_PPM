from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from shop.models import Cart  # importa Cart dal modulo dove l'hai definito

User = get_user_model()

@receiver(post_save, sender=User)
def crea_carrello_automatico(sender, instance, created, **kwargs):
    if created:
        Cart.objects.create(user=instance)
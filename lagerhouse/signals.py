import logging
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

logger = logging.getLogger(__name__)

@receiver(post_save, sender=User)
def create_auth_token(instance=None, created=False, **kwargs):
    if created:
        logger.info(f"Creating token for user: {instance.username}")
        Token.objects.get_or_create(user=instance)
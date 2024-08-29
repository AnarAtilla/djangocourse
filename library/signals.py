# library/signals.py
from django.contrib.auth.models import User
from django.db.models.signals import post_delete
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from .models import Author, Book, Member, Borrow


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
@receiver(post_save, sender=Author)
def author_post_save(sender, instance, created, **kwargs):
    if created:
        print(f"New author created: {instance}")
    else:
        print(f"Author updated: {instance}")

@receiver(post_delete, sender=Author)
def author_post_delete(sender, instance, **kwargs):
    print(f"Author deleted: {instance}")

# Добавьте аналогичные обработчики для других моделей
@receiver(post_save, sender=Book)
def book_post_save(sender, instance, created, **kwargs):
    if created:
        print(f"New book created: {instance}")
    else:
        print(f"Book updated: {instance}")

@receiver(post_delete, sender=Book)
def book_post_delete(sender, instance, **kwargs):
    print(f"Book deleted: {instance}")

# Продолжайте добавлять обработчики для остальных моделей
# Например, для Member:
@receiver(post_save, sender=Member)
def member_post_save(sender, instance, created, **kwargs):
    if created:
        print(f"New member created: {instance}")
    else:
        print(f"Member updated: {instance}")

@receiver(post_delete, sender=Member)
def member_post_delete(sender, instance, **kwargs):
    print(f"Member deleted: {instance}")

@receiver(post_save, sender=Borrow)
def borrow_post_save(sender, instance, created, **kwargs):
    print("borrow_post_save called")
    if created:
        print(f"New borrow created: {instance}")
    else:
        print(f"Borrow updated: {instance}")
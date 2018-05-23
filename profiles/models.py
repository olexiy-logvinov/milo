from random import randint
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthday = models.DateField(blank=True, null=True)
    randint = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_profile(instance, **kwargs):
    Profile.objects.create(
        user=instance,
        birthday=kwargs.get('birthday', None),
        randint=randint(1, 100)
    )

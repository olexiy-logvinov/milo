from random import randint
from datetime import timedelta
from django.db import models, IntegrityError
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.utils import timezone


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthday = models.DateField(blank=True, null=True)
    randint = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.user.username

    def allowed(self):
        if not self.birthday:
            return False
        # https://stackoverflow.com/questions/765797/python-timedelta-in-years
        # I assume this timedelta approximation is acceptable in this case.
        years = 13
        return timezone.now().date() - self.birthday > timedelta(seconds=years*365.25*24*60*60) - timedelta(hours=24)
        #     return 'allowed'
        # return 'blocked'

    def bizz_fuzz(self):
        bizz = self.randint % 3 == 0
        fuzz = self.randint % 5 == 0
        if bizz and fuzz:
            return 'BizzFuzz'
        elif bizz:
            return 'Bizz'
        elif fuzz:
            return 'Fuzz'
        return ''


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(
            user=instance,
            randint=randint(1, 100)
        )


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

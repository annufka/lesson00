from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from pytz import unicode


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')
    phone = models.CharField(max_length=20, blank=True, null=True)
    age = models.IntegerField(default=0)
    code = models.IntegerField(default=0)
    active = models.BooleanField(default=False)
    photo = models.ImageField('logo', null=True, blank=True, upload_to='logo')

    def __str__(self):
        return unicode(str(self.user))

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

class Currency(models.Model):
    name = models.CharField(max_length=20)
    value = models.CharField(max_length=20)
    data_type = models.DateField(blank=True, null=True)

    def __str__(self):
        return unicode(str(self.name))
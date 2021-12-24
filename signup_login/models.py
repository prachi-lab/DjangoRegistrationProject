from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    username=models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)

    def __str__(self):
          return "%s's profile" % self.user

def create_user_profile(sender, instance, created, **kwargs):
    if created:
       profile, created = UserProfile.objects.get_or_create(user=instance)

post_save.connect(create_user_profile, sender=User)
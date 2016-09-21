from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User)

    def __str__(self):return self.user.username

    class Meta:
        verbose_name = 'USER PROFILE'

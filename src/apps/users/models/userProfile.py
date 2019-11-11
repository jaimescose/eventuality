from django.db import models

from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, default='')
    birthdate = models.DateTimeField(null=True, blank=True, default=None)

    def __str__(self):
        return format(self.user.username)

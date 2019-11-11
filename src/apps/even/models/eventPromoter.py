import pandas
from django.db import models

def get_default_joined_date():
    return pandas.to_datetime('today')

class EventPromoter(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    joined_date = models.DateTimeField(default=get_default_joined_date)
    admin_users = models.ManyToManyField('users.UserProfile', related_name='admin_users')

    def __str__(self):
        return self.name

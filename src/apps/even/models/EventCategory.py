from django.db import models

class EventCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    parent_category = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Event Category'
        verbose_name_plural = 'Event Categories'

    def __str__(self):
        return self.name

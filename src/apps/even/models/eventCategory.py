from django.db import models


class EventCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    default = models.BooleanField(default=False)
    parent_category = models.ForeignKey(
        'self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Event category'
        verbose_name_plural = 'Event categories'

    def __str__(self):
        return self.name

    @classmethod
    def get_default_category(cls):
        return cls.objects.get(default=True)

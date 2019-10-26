from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=100)
    longitue = models.DecimalField(max_digits=9, decimal_places=6)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    from_datetime = models.DateTimeField()
    to_datetime = models.DateTimeField(blank=True, null=True)
    main_category = models.ForeignKey('even.EventCategory', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

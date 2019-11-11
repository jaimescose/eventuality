from django.db import models

from apps.even.models.eventCategory import EventCategory

class Event(models.Model):
    name = models.CharField(max_length=100)
    longitue = models.DecimalField(max_digits=9, decimal_places=6)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    from_datetime = models.DateTimeField()
    to_datetime = models.DateTimeField(blank=True, null=True)
    main_category = models.ForeignKey('even.EventCategory', 
                                    default=EventCategory.get_default_category, 
                                    on_delete=models.SET_DEFAULT)
    subcategories = models.ManyToManyField('even.EventCategory', 
                                        related_name='subcategories',
                                        blank=True,
                                        default=None)

    promoter = models.ForeignKey('even.EventPromoter', default=None, on_delete=models.PROTECT)

    co_promoters = models.ManyToManyField('even.EventPromoter', 
                                        related_name='co_promoters', 
                                        blank=True, 
                                        default=None)

    def __str__(self):
        return self.name

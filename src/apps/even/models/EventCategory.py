from django.db import models

class EventCategory(models.Model):
    CATEOGRIES = [
        (0, 'Music'),
        (1, 'Film'),
        (2, 'Lectures & Books'),
        (3, 'Fashion'),
        (4, 'Music'),
        (5, 'Visual Arts'),
        (6, 'Performing Arts'),
        (7, 'Film'),
        (8, 'Lectures & Books'),
        (9, 'Fashion'),
        (10, 'Food & Drink'),
        (11, 'Festivals & Fairs'),
        (12, 'Charities'),
        (13, 'Sports & Active Life'),
        (15, 'Nightlife'),
        (16, 'Kids & Family'),
        (17, 'Other')
    ]

    name = models.PositiveSmallIntegerField(choices=CATEOGRIES)
    description = models.TextField()

from django.contrib import admin

from apps.even.models.eventPromoter import EventPromoter

class EventPromoterAdmin(admin.ModelAdmin):
    ordering = ['name']

admin.site.register(EventPromoter, EventPromoterAdmin)

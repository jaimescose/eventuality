from django.contrib import admin
from apps.even.models.event import Event

class EventAdmin(admin.ModelAdmin):
    ordering = ['name']

admin.site.register(Event, EventAdmin)

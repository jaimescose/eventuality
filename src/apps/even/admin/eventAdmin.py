from django.contrib import admin
from apps.even.models.event import Event

class EventAdmin(admin.ModelAdmin):
    list_display = ['name', 'main_category']
    ordering = ['name']

admin.site.register(Event, EventAdmin)

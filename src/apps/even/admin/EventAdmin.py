from django.contrib import admin
from apps.even.models.Event import Event

class EventAdmin(admin.ModelAdmin):
    list_display = ['name', 'main_category']
    ordering = ['name']

admin.site.register(Event, EventAdmin)

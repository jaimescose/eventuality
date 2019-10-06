from django.contrib import admin
from apps.even.models.EventCategory import EventCategory

class EventCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    ordering = ['name']

admin.site.register(EventCategory, EventCategoryAdmin)

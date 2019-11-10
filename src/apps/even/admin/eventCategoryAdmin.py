from django.contrib import admin
from apps.even.models.eventCategory import EventCategory

class EventCategoryAdmin(admin.ModelAdmin):
    ordering = ['name']

admin.site.register(EventCategory, EventCategoryAdmin)

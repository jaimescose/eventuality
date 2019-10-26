import graphene
from graphene_django.types import DjangoObjectType

from apps.even.models.event import Event
from apps.even.models.eventCategory import EventCategory

class EventCategoryType(DjangoObjectType):
    class Meta:
        model = EventCategory

class EventType(DjangoObjectType):
    class Meta:
        model = Event
 
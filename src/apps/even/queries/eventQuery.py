import graphene
from graphene_django.types import ObjectType

from apps.even.types import EventType

from apps.even.models.event import Event

class Query(ObjectType):
    event = graphene.Field(EventType, id=graphene.Int())
    events = graphene.List(EventType)

    def resolve_event(self, info, **kwargs):
        id = kwargs.get('id')

        try:
            return Event.objects.get(id=id)
        except Event.DoesNotExist:
            return None

    def resolve_events(self, info, **kwargs):
        return Event.objects.all()

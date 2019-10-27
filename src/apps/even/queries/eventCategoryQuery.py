import graphene
from graphene_django.types import ObjectType

from apps.even.types import EventCategoryType

from apps.even.models.eventCategory import EventCategory

# Create a Query type for EventCategory model
class Query(ObjectType):
    event_category = graphene.Field(EventCategoryType, id=graphene.Int())
    event_categories = graphene.List(EventCategoryType)

    def resolve_event_category(self, info, **kwargs):
        id = kwargs.get('id')

        try:
            return EventCategory.objects.get(id=id)
        except EventCategory.DoesNotExist as e:
            return None

    def resolve_event_categories(self, info, **kwargs):
        return EventCategory.objects.all()

schema = graphene.Schema(query=Query)

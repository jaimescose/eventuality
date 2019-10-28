import graphene

from apps.even.types import EventCategoryType
from apps.even.inputs import EventCategoryInput

from apps.even.models.eventCategory import EventCategory

class CreateEventCategory(graphene.Mutation):
    class Arguments:
        input = EventCategoryInput(required=True)

    ok = graphene.Boolean()
    event_category = graphene.Field(EventCategoryType)

    def mutate(root, info, input=None):
        # initialize return values
        ok = False
        event_category = None

        try:
            # could not exist more than one category with the same name
            event_category = EventCategory.objects.get(name=input.name)

            return CreateEventCategory(ok=ok, event_category=event_category)
        except EventCategory.DoesNotExist as e:
            kwargs = {
                'name': input.name,
                'description': input.description,
                'parent_category': input.parent_category
            }

            event_category = EventCategory.objects.create(**kwargs)

            return CreateEventCategory(ok=ok, event_category=event_category)

class Mutation(graphene.ObjectType):
    create_event_category = CreateEventCategory.Field()

schema = graphene.Schema(mutation=Mutation)

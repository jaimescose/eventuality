import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from apps.even.models import Promoter, Event

# Create a GraphQL type for the promoter model
class PromoterType(DjangoObjectType):
    class Meta:
        model = Promoter

# Create a GraphQL type for the Event model
class EventType(DjangoObjectType):
    class Meta:
        model = Event

# Create a Query type
class Query(ObjectType):
    promoter = graphene.Field(PromoterType, id=graphene.Int())
    event = graphene.Field(EventType, id=graphene.Int())
    promoters = graphene.List(PromoterType)
    events= graphene.List(EventType)

    def resolve_promoter(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Promoter.objects.get(pk=id)

        return None

    def resolve_event(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Event.objects.get(pk=id)

        return None

    def resolve_promoters(self, info, **kwargs):
        return Promoter.objects.all()

    def resolve_events(self, info, **kwargs):
        return Event.objects.all()

class PromoterInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()

class EventInput(graphene.InputObjectType):
    id = graphene.ID()
    title = graphene.String()
    promoters = graphene.List(PromoterInput)
    year = graphene.Int()


class CreatePromoter(graphene.Mutation):
    class Arguments:
        input = PromoterInput(required=True)

    ok = graphene.Boolean()
    promoter = graphene.Field(PromoterType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        promoter_instance = Promoter(name=input.name)
        promoter_instance.save()
        return CreatePromoter(ok=ok, promoter=promoter_instance)

class CreateEvent(graphene.Mutation):
    class Arguments:
        input = EventInput(required=True)

    ok = graphene.Boolean()
    event = graphene.Field(EventType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        promoters = []
        for promoter_input in input.promoter:
          promoter = Promoter.objects.get(pk=promoter_input.id)
          if promoter is None:
            return CreateEvent(ok=False, event=None)
          promoters.append(promoter)
        event_instance = Event(
          title=input.title,
          year=input.year
          )
        event_instance.save()
        event_instance.promoters.set(promoters)
        return CreateEvent(ok=ok, event=event_instance)

class Mutation(graphene.ObjectType):
    create_promoter = CreatePromoter.Field()
    create_event = CreateEvent.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)

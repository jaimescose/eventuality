import graphene

from apps.even.mutations import *
from apps.even.queries import *


class Query(eventQuery.Query, eventCategoryQuery.Query, graphene.ObjectType):
    pass

class Mutation(eventCategoryMutation.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)

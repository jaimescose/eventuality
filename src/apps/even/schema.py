import graphene

from apps.even.queries import *

class Query(eventCategoryQuery.Query, graphene.ObjectType):
    pass

class Mutation(graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)

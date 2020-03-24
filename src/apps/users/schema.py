import graphene

from apps.users.queries import *
from apps.users.mutations import *

class Query(
    userQuery.Query, 
    graphene.ObjectType):
    pass

class Mutation(
    userMutation.Mutation, 
    graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)

import graphene
import apps.even.schema as even
import apps.users.schema as users

class Query(
    even.schema.Query, 
    users.schema.Query,
    graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass

class Mutation(
    even.Mutation, 
    users.Mutation,
    graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)

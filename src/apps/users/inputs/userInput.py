import graphene

class UserInput(graphene.InputObjectType):
    id = graphene.Int()
    email = graphene.String(required=True)
    username = graphene.String(required=True)
    password = graphene.String(required=True)
    first_name = graphene.String(required=False)
    last_name = graphene.String(required=False)
    bio = graphene.String(required=False)
    birthdate = graphene.DateTime(required=False)

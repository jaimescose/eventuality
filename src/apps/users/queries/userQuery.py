import graphene
from graphene_django.types import ObjectType

from apps.users.types.userType import UserType

from apps.users.models.userProfile import UserProfile

class Query(ObjectType):
    users = graphene.List(UserType)

    def resolve_users(parent, info, **kwargs):
        return UserProfile.objects.all()

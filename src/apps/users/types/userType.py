import graphene
from graphene_django.types import DjangoObjectType

from django.contrib.auth import get_user_model

from apps.users.models.userProfile import UserProfile

class DjangoUserType(DjangoObjectType):
    class Meta:
        model = get_user_model()


class UserType(DjangoObjectType):
    class Meta:
        model = UserProfile
        description = "This type includes an user profile and the related user"

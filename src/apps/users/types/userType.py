from django.contrib.auth import get_user_model

import graphene
from graphene_django.types import DjangoObjectType

from apps.users.models.userProfile import UserProfile

class DjangoUserType(graphene.Interface):
    class Meta:
        model = get_user_model

class UserType(DjangoObjectType):
    class Meta:
        interfaces = (DjangoUserType)
        model = UserProfile

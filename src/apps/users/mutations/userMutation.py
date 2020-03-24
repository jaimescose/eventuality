import graphene

from apps.users.inputs.userInput import UserInput

from apps.users.types.userType import UserType

from apps.users.models.userProfile import UserProfile

from django.contrib.auth import get_user_model
from apps.users.models.userProfile import UserProfile

class CreateUser(graphene.Mutation):
    class Arguments:
        input = UserInput(required=True)

    ok = graphene.Boolean()
    message = graphene.String()
    user = graphene.Field(UserType)

    def mutate(root, info, input=None):
        # initialize returned objects
        ok = False
        message = ''
        user = None

        # this one is the default user model of django
        user_model = get_user_model()

        # username must be unique
        if user_model.objects.filter(username=input.username).exists():
            message = 'username already taken'.format(input.username)

            return CreateUser(ok=ok, message=message, user=user)

        # email must be unique
        if user_model.objects.filter(email=input.email).exists():
            message = 'email already taken'.format(input.email)

            return CreateUser(ok=ok, message=message, user=user)

        # create django user
        user_kwargs = {
            'email': input.email,
            'username': input.username,
            'first_name': input.first_name,
            'last_name': input.last_name
        }
        user_model.objects.create(**user_kwargs)

        # get the new user and set password
        user = user_model.objects.get(username=input.username)
        user.set_password(input.password)
        user.save()

        # get the user profile created because of the user 'post_save' signal
        user_profile = UserProfile.objects.get(user=user)

        # update user profile
        user_profile_kwargs = {
            'bio': input.bio,
            'birthdate': input.birthdate
        }

        user_profile.update(**user_profile_kwargs)
        user_profile.save()

        message = 'user succesfully created'

        return CreateUser(ok=ok, message=message, user=user_profile)

class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()

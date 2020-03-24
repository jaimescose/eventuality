from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from apps.even.models.userProfile import UserProfile

class UserProfileInline(admin.TabularInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Profile'
    # fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = [
        UserProfileInline,
        ]

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

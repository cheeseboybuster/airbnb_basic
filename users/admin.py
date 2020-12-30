from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    # see https://docs.djangoproject.com/en/3.1/ref/contrib/admin/ for detail for 'model admin'
    # admin.site.register(models.User, CustomUserAdmin) 이 결국 같은 commend

    """ Custom User Admin """
    fieldsets = UserAdmin.fieldsets + (
        ("Custom Profile",
         {"fields": (
             "avatar", "gender", "bio", "birthdate", "language", "currency", "superhost",)
          },
         ),
    )

from django.contrib import admin
from .models import games,User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.

admin.site.register(games)


@admin.register(User)
class UserAdmin(BaseUserAdmin):
     add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ('username', 'email',
            'password', 'Gender','Date_of_birth')
            },
        ),
    )
     list_display=['id', 'username', 'email',
             'Gender','Date_of_birth']


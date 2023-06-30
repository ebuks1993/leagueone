from django.contrib import admin
from .models import User,Games,Pitch,Sport,GameSelect,Agerange
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.

admin.site.register(Games)
admin.site.register(GameSelect)
admin.site.register(Pitch)
admin.site.register(Sport)
admin.site.register(Agerange)


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


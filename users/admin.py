from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'bio')}),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'is_banned',
                'groups', 'user_permissions'
            )
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username', 'email', 'password1', 'password2',
                'is_active', 'is_staff', 'is_superuser',
                 'is_banned'
            ),
        }),
    )

    list_display = ['username', 'email', 'is_superuser', 'is_staff', 'is_banned']
    list_filter = ['is_staff', 'is_superuser', 'is_banned']

admin.site.register(CustomUser, CustomUserAdmin)
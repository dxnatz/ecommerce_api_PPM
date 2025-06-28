from django.contrib import admin

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        ('Ruoli personalizzati', {'fields': ('bio', 'is_moderator', 'is_banned')}),
    )

    list_display = ['username', 'email', 'is_staff', 'is_moderator', 'is_banned']

    list_filter = ['is_staff', 'is_superuser', 'is_moderator', 'is_banned']

readonly_fields = []

admin.site.register(CustomUser, CustomUserAdmin)

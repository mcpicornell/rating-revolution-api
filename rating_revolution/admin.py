from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


class UserAdmin(BaseUserAdmin):

    list_display = ('id', 'email', 'is_active', 'is_staff')
    list_filter = ('is_active', 'is_staff')
    ordering = ('id', 'email',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff')}),
    )


admin.site.register(User, UserAdmin)


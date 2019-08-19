from django.contrib import admin

from accounts.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'user_type', 'is_mature', 'driver_is_free']
    search_fields = ['user__username']
    list_filter = ['user_type',]

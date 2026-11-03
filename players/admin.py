
from django.contrib import admin

from .models import PlayerProfile


@admin.register(PlayerProfile)
class PlayerProfileAdmin(admin.ModelAdmin):
    list_display = ("full_name", "position", "region", "guardian_approved")
    list_filter = ("position", "region", "guardian_approved")
    search_fields = ("full_name", "town", "current_team")

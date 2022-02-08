from django.contrib import admin

from .models import Position


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('name', 'matching_positions', 'city',)

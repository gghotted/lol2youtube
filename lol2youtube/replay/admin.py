from django.contrib import admin

from replay.models import PentakillReplay


@admin.register(PentakillReplay)
class PentakillReplayAdmin(admin.ModelAdmin):
    list_display = (
        'created',
        'champion',
    )

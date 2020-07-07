from django.contrib import admin
from . import models


@admin.register(models.Reservation)
class RedervationAdmin(admin.ModelAdmin):

    list_display = (
        "room",
        "guest",
        "status",
        "check_in",
        "check_out",
        "in_progress",
        "is_finished",
    )

from django.contrib import admin
from . import models
from reviews.models import Review
from django.utils.html import format_html


@admin.register(models.RoomType, models.Amenity, models.Facility, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "used_by",
    )

    def used_by(self, obj):
        return obj.rooms.count()


class photoInline(admin.TabularInline):
    model = models.Photo


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    inlines = [
        photoInline,
    ]

    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "city", "country", "description", "price")},
        ),
        ("Time", {"fields": ("check_in", "check_out", "instant_book")},),
        ("Space", {"fields": ("guests", "beds", "bedrooms", "baths")},),
        ("More Details", {"fields": ("amenities", "facilities", "house_rule")},),
        ("Last Details", {"fields": ("host",)},),
    )

    list_display = (
        "name",
        "country",
        "city",
        "price",
        "address",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities",
        "count_photos",
        "total_rating",
    )

    list_filter = (
        "host__superhost",
        "room_type",
        "amenities",
        "facilities",
        "house_rule",
        "city",
        "instant_book",
        "country",
    )

    ordering = ["price", "beds"]

    search_fields = ["city"]

    filter_horizontal = (
        "amenities",
        "facilities",
        "house_rule",
    )

    raw_id_fields = ("host",)

    def count_amenities(self, obj):
        return obj.amenities.count()

    def count_photos(self, obj):
        return obj.photos.count()


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    list_display = (
        "__str__",
        "get_Thumbnail",
    )

    def get_Thumbnail(self, obj):
        return format_html(
            '<img width="100" src="{}" alt="{}" />', obj.file.url, obj.caption,
        )

    get_Thumbnail.short_description = "Thumbnail"

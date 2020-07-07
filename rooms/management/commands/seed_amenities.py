from django.core.management.base import BaseCommand, CommandError
from rooms.models import Amenity


class Command(BaseCommand):

    help = "This command creates amenities"

    """
    def add_arguments(self, parser):

        parser.add_argument(
            "--times", help="test for showing show me the money.",
        )
        """

    def handle(self, *labels, **options):
        amenities = [
            "air conditioning",
            "Kitchen",
            "Shampoo",
            "Heating",
            "Air conditioning",
            "Washer",
            "Dryer",
            "Wifi",
            "Breakfast",
            "Indoor fireplace",
            "Hangers",
            "Iron",
            "Hair dryer",
            "Laptop-friendly workspace",
            "TV",
            "Crib",
            "High chair",
            "Self check-in",
            "Smoke alarm",
            "Carbon monoxide alarm",
            "Private bathroom",
        ]

        for a in amenities:
            Amenity.objects.create(name=a)
        self.stdout.write(self.style.SUCCESS("Amenities created!!!"))

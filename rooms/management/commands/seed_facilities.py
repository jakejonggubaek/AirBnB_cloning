from django.core.management.base import BaseCommand, CommandError
from rooms.models import Facility


class Command(BaseCommand):

    help = "This command creates Facilities"

    """
    def add_arguments(self, parser):

        parser.add_argument(
            "--times", help="test for showing show me the money.",
        )
        """

    def handle(self, *labels, **options):
        facilities = [
            "Free parking on premises",
            "Gym",
            "Hot tub",
            "Pool",
        ]

        for f in facilities:
            Facility.objects.create(name=f)
        self.stdout.write(
            self.style.SUCCESS(f"{len(facilities)} Facilities created!!!")
        )

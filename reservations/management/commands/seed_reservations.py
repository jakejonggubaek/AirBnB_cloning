import random
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand, CommandError
from django.contrib.admin.utils import flatten
from reservations import models as reservation_models
from users import models as user_models
from rooms import models as room_models
from django_seed import Seed


class Command(BaseCommand):

    help = "This command creates reservations"

    def add_arguments(self, parser):

        parser.add_argument(
            "--number",
            default=1,
            type=int,
            help="type how many lists you would like to make",
        )

    def handle(self, *labels, **options):

        number = options.get("number")
        seeder = Seed.seeder()
        users = user_models.User.objects.all()
        rooms = room_models.Room.objects.all()

        seeder.add_entity(
            reservation_models.Reservation,
            number,
            {
                "guest": lambda x: random.choice(users),
                "room": lambda x: random.choice(rooms),
                "status": lambda x: random.choice(["pending", "confirmed", "canceled"]),
                "check_in": lambda x: datetime.now(),
                "check_out": lambda x: datetime.now()
                + timedelta(days=random.randint(2, 30)),
            },
        )

        seeder.execute()

        self.stdout.write(self.style.SUCCESS(f"{number} of reservations are created!"))

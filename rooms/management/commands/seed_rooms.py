import random
from django.core.management.base import BaseCommand, CommandError
from django.contrib.admin.utils import flatten
from rooms import models as room_models
from users import models as user_models
from django_seed import Seed


class Command(BaseCommand):

    help = "This command creates users"

    def add_arguments(self, parser):

        parser.add_argument(
            "--number",
            default=1,
            type=int,
            help="type how many users you would like to make",
        )

    def handle(self, *labels, **options):

        number = options.get("number")
        seeder = Seed.seeder()
        all_users = user_models.User.objects.all()
        room_type = room_models.RoomType.objects.all()
        seeder.add_entity(
            room_models.Room,
            number,
            {
                "name": lambda x: seeder.faker.address(),
                "host": lambda x: random.choice(all_users),
                "room_type": lambda x: random.choice(room_type),
                "price": lambda x: random.randint(10, 500),
                "guests": lambda x: random.randint(1, 15),
                "beds": lambda x: random.randint(1, 10),
                "bedrooms": lambda x: random.randint(1, 10),
                "baths": lambda x: random.randint(1, 5),
                "check_in": lambda x: random.choice(("13:00", "14:00", "15:00")),
                "check_out": lambda x: random.choice(("11:00", "12:00", "13:00")),
            },
        )

        created_photo = seeder.execute()
        created_clean = flatten(list(created_photo.values()))
        amenities = room_models.Amenity.objects.all()
        facilities = room_models.Facility.objects.all()
        rules = room_models.HouseRule.objects.all()

        for pk in created_clean:
            room = room_models.Room.objects.get(pk=pk)
            for i in range(random.randint(3, 5)):
                room_models.Photo.objects.create(
                    caption=seeder.faker.sentence(),
                    room=room,
                    file=f"room_photos/{random.randint(1, 31)}.webp",
                )
            for a in amenities:
                magic_number = random.randint(0, 15)
                if magic_number % 2 == 0:
                    room.amenities.add(a)

            for f in facilities:
                magic_number = random.randint(0, 15)
                if magic_number % 2 == 0:
                    room.facilities.add(f)

            for h in rules:
                magic_number = random.randint(0, 15)
                if magic_number % 2 == 0:
                    room.house_rule.add(h)

        self.stdout.write(self.style.SUCCESS(f"{number} of room/rooms are created!"))

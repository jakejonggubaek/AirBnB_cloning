from django.core.management.base import BaseCommand, CommandError
from users.models import User
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
        seeder.add_entity(User, number, {"is_staff": False, "is_superuser": False,})
        seeder.execute()

        self.stdout.write(self.style.SUCCESS(f"{number} of user/users are created!"))

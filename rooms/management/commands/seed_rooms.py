import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from users import models as user_models
from rooms import models as room_models


class Command(BaseCommand):
    help = "This command seeds rooms"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=1,
            type=int,
            help="How many rooms do you want to create?",
        )

    def handle(self, *args, **options):
        number = options.get("number", 1)
        seeder = Seed.seeder()
        all_users = user_models.User.objects.all()
        room_types = room_models.RoomType.objects.all()
        seeder.add_entity(
            room_models.Room,
            number,
            {
                "name": lambda x: seeder.faker.address(),
                "host": lambda x: random.choice(all_users),
                "room_type": lambda x: random.choice(room_types),
                "price": lambda x: random.randint(0, 500),
                "guests": lambda x: random.randint(0, 5),
                "beds": lambda x: random.randint(0, 5),
                "bedrooms": lambda x: random.randint(0, 5),
                "baths": lambda x: random.randint(0, 5),
            },
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} Rooms Made!"))
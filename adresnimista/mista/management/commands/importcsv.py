import csv

from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Imports addresses from provided CSVs"

    def handle(self, *args, **options):
        csv.register_dialect("address", delimiter=";")

        for filename in (settings.BASE_DIR / "csv").glob("*.csv"):
            with filename.open(newline="", encoding="windows-1250") as f:
                rows = csv.DictReader(f, dialect="address")

                for row in rows:
                    print(row)
                break

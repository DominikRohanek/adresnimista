import csv

from django.conf import settings
from django.core.management.base import BaseCommand
from adresnimista.mista.models import City, Address


class Command(BaseCommand):
    help = "Imports addresses from provided CSVs"

    def handle(self, *args, **options):
        csv.register_dialect("address", delimiter=";")

        cities = {}
        Address.objects.all().delete()

        for filename in (settings.BASE_DIR / "csv").glob("*.csv"):
            addresses = []

            with filename.open(newline="", encoding="windows-1250") as f:
                rows = csv.DictReader(f, dialect="address")

                for row in rows:
                    name = row["Název obce"]
                    postalcode = row["PSČ"]

                    if (name, postalcode) in cities:
                        city = cities[(name, postalcode)]
                    else:
                        city, created = City.objects.get_or_create(
                            name=name, postalcode=postalcode
                        )
                        cities[(name, postalcode)] = city

                    address = Address(
                        city=city,
                        street=row["Název ulice"],
                        orientation_number=row["Číslo orientační"]
                        + row["Znak čísla orientačního"],
                        descriptive_number=row["Číslo domovní"],
                    )
                    addresses.append(address)
            Address.objects.bulk_create(addresses)

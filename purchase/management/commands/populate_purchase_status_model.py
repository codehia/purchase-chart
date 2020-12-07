import random
from django.core.management.base import BaseCommand, CommandError
from purchase.models import PurchaseStatusModel, PurchaseModel
from dateutil import parser
from faker import Faker


CHOICES = (
    ("open", "Open"),
    ("verified", "Verified"),
    ("dispatched", "Dispatched"),
    ("delivered", "Delivered"),
)
START_DATE = parser.parse("01st Jan 2019 05 pm")
END_DATE = parser.parse("31st March 2020 10 pm")


class Command(BaseCommand):
    def _create_fake_status_data(self, purchase_data):
        purchase_status_data = []
        number_of_statuses = range(1, random.randint(1, 4))
        for choice_id in number_of_statuses:
            fake = Faker()
            created_at = fake.date_between_dates(START_DATE, END_DATE)
            purchase_status_data.append(
                PurchaseStatusModel(
                    purchase=purchase_data,
                    status=CHOICES[choice_id][0],
                    created_at=created_at,
                )
            )
        return purchase_status_data

    def handle(self, *args, **options):
        purchase_data_queryset = PurchaseModel.objects.all()
        purchase_status_data_final = []
        for purchase_data in purchase_data_queryset:
            purchase_status_data_final.extend(
                self._create_fake_status_data(purchase_data)
            )
        PurchaseStatusModel.objects.bulk_create(purchase_status_data_final)

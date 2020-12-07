from django.core.management.base import BaseCommand, CommandError
from purchase.models import PurchaseModel


class Command(BaseCommand):
    def handle(self, *args, **options):
        people_name = [
            "john",
            "andy",
            "alice",
            "craig",
            "daniel",
            "shivaini",
            "nishant",
            "sloss",
            "sachin",
            "nikhil",
        ]
        purchase_data = []
        for index, (first_purchaser, second_purchaser) in enumerate(
            zip(people_name[:5], people_name[5:])
        ):
            for qty in [index + 1] * 500:
                purchase_data.append(
                    PurchaseModel(purchaser_name=first_purchaser, quantity=qty)
                )
                purchase_data.append(
                    PurchaseModel(purchaser_name=second_purchaser, quantity=14 - qty)
                )
                print(f"adding data for {first_purchaser} {second_purchaser}")
        PurchaseModel.objects.bulk_create(purchase_data)


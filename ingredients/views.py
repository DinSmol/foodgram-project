import csv
from ingredients.models import Ingredient


def data_upl(request):
    with open('ingredients.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            _, created = Ingredient.objects.get_or_create(
                name=row[0],
                units=row[1],
                )

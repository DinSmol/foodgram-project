from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=64)
    units = models.CharField(max_length=20)

    def __str__(self):
        return self.name

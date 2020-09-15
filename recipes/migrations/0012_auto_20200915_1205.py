# Generated by Django 3.0.3 on 2020-09-15 12:05

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipes', '0011_recipe_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='favourite',
            field=models.ManyToManyField(blank=True, related_name='fav_recipes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Favourite',
        ),
    ]

# Generated by Django 3.0.3 on 2020-09-12 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_auto_20200912_0630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipeingredient',
            name='quantity',
            field=models.IntegerField(blank=True),
        ),
    ]

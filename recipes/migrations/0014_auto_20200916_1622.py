# Generated by Django 3.0.3 on 2020-09-16 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0013_auto_20200915_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(blank=True, upload_to='recipes/'),
        ),
    ]

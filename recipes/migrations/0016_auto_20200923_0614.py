# Generated by Django 3.0.3 on 2020-09-23 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0015_auto_20200923_0614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='tag_name_eng',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Name'),
        ),
    ]

# Generated by Django 3.0.3 on 2020-09-10 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ingredients', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredient',
            name='quantity',
        ),
    ]

# Generated by Django 4.0.5 on 2022-06-14 21:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('googlesheet', '0004_rename_orders_order'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Order',
        ),
    ]

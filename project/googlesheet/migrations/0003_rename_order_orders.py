# Generated by Django 4.0.5 on 2022-06-14 21:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('googlesheet', '0002_rename_orders_order'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Order',
            new_name='Orders',
        ),
    ]

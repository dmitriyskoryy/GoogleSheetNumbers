# Generated by Django 4.0.5 on 2022-06-16 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('googlesheet', '0012_alter_order_deliverytime_alter_order_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='number',
            field=models.SmallIntegerField(verbose_name='№'),
        ),
    ]

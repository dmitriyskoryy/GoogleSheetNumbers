# Generated by Django 4.0.5 on 2022-06-15 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('googlesheet', '0008_alter_order_deliverytime_alter_order_priceconvert'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='priceConvert',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=20, verbose_name='стоимость в руб.'),
        ),
    ]

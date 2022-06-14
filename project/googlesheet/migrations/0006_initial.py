# Generated by Django 4.0.5 on 2022-06-14 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('googlesheet', '0005_delete_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.TextField(verbose_name='№')),
                ('orderNumber', models.TextField(verbose_name='заказ №')),
                ('price', models.TextField(verbose_name='стоимость,$')),
                ('priceConvert', models.TextField(verbose_name='стоимость,₽')),
                ('deliveryTime', models.DateField(verbose_name='срок поставки')),
            ],
        ),
    ]
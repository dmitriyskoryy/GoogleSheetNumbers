
from django.db import models


class Order(models.Model):
    """Таблица Заказы в БД"""


    number = models.SmallIntegerField(verbose_name="№")

    orderNumber = models.CharField(max_length=128, verbose_name="заказ №")

    price = models.CharField(max_length=128, verbose_name="стоимость,$")

    priceConvert = models.CharField(max_length=128, verbose_name="стоимость в руб.")

    deliveryTime = models.CharField(max_length=10, verbose_name="срок поставки")
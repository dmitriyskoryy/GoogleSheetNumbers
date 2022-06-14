from django.contrib.postgres.fields import ArrayField
from django.db import models


class Order(models.Model):
    """Заказы"""


    number = models.TextField(verbose_name="№")

    orderNumber = models.TextField(verbose_name="заказ №")

    price = models.DecimalField(max_digits=20, decimal_places=2, verbose_name="стоимость,$")

    priceConvert = models.DecimalField(max_digits=20, decimal_places=2, verbose_name="стоимость,₽", default=0)

    deliveryTime = models.DateField(verbose_name="срок поставки")
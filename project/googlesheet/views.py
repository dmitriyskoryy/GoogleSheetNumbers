
from django.core.exceptions import ObjectDoesNotExist
from django.views import generic
from .models import Order

from .googlesheets import GoogleSheets
from .currency import get_currency
from .deadline import get_deadline_orders


class OrderList(generic.ListView):
    model = Order
    template_name = 'order_list.html'
    context_object_name = 'orderlist'
    ordering = ['number']

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        if self.request.GET.get("update_data"):
            display_orders()
        # context['title'] =
        return context




def get_order_db(wsh):
    """Получение записи из БД по номеру заказа (по полю orderNumber)"""
    try:
        order = Order.objects.get(orderNumber=wsh)
        return order
    except ObjectDoesNotExist:
        return None



def add_order(wsh, rate):
    """Добавление нового заказа (строки) в БД"""
    Order.objects.create(
        number=wsh[0],
        orderNumber=wsh[1],
        price=wsh[2],
        priceConvert=rate,
        deliveryTime=wsh[3]
    )


def update_order(wsh, rate):
    """Обновление заказа (строки) в БД"""
    order = get_order_db(wsh[1])

    if order:
        order.number = wsh[0]
        order.orderNumber = wsh[1]
        order.price = wsh[2]
        order.priceConvert = rate
        order.deliveryTime = wsh[3]
        order.save()



def delete_order(wsh):
    """Удаление заказа из БД, если заказа с таким номером нет в таблице гугл"""
    list_gsh = []
    for _ in wsh:
        list_gsh.append(_[1])

    orders_db = [order_num.orderNumber for order_num in Order.objects.all()]
    for order_num in orders_db:
        if order_num not in list_gsh:
            order = get_order_db(order_num)
            if order:
                order.delete()


def price_convert(wsh, rate):
    """Функция конвертирует в рубли"""
    try:
        price = float(wsh) * float(rate)  # конвертируем в рубли
        res = float("{0:.2f}".format(price)) # оставляем в числе два знака после точки
        return str(res)
    except ValueError:
        print("Invalid Float number to be converted. ")




def display_orders():
    """Функция обновляет содержимое таблицы на странице клиента"""

    # получаем рабочий лист с данными из таблицы гугл
    worksheet = GoogleSheets().get_worksheet()

    # получаем текущий курс доллара
    rate = get_currency().replace(',', '.')

    for wsh in worksheet.get_all_values()[1::]:
        priceConvert = price_convert(wsh[2], rate)
        if Order.objects.filter(orderNumber=wsh[1]):
            # если номер заказа из таблицы гугл есть в БД, то обновляем заказ в БД
            update_order(wsh, priceConvert)
        else:
            # если номера заказа из таблицы гугл нет в БД, то добавляем заказ в БД
            add_order(wsh, priceConvert)

    # удаляем из БД строки, которых нет в таблице гугл
    delete_order(worksheet.get_all_values()[1::])

    # получения тех заказов, 'срок поставки' которых прошел и отправка сведений о них в телеграм
    get_deadline_orders()



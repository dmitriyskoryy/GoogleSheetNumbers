"""Модуль проверки соблюдения «срока поставки» из таблицы.
В случае, если срок прошел, отправляет уведомление в Telegram"""
from datetime import datetime
import telebot

from .models import Order


token = "ваш токен"
bot = telebot.TeleBot(token)

def get_deadline_orders():
    """Функция получения тех заказов, 'срок поставки' которых прошел"""
    datetimeNow = datetime.now()
    for order in Order.objects.all():
        deliveryTime = datetime.strptime(order.deliveryTime, '%d.%m.%Y')
        if datetimeNow > deliveryTime:
            send_message_in_telegram(order)


def send_message_in_telegram(order):
    """Функция отправки сообщения в телеграм"""
    chatId = '915838357'
    text = f"deadline: заказ № {order.orderNumber}, стоимость {order.price}$,  срок поставки {order.deliveryTime}"
    bot.send_message(chatId, text=text)



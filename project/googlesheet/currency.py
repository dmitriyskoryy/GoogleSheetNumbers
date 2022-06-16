"""Модуль для получения курса доллара с ресурса ЦБ РФ и распарсивания его из XML"""

import requests
import xml.etree.ElementTree as ET



def get_currency():
    """Запрос на Api ЦБ РФ и возвращает курс доллара США"""
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    res = requests.get(url)

    with open('cur.xml', 'w') as file:
        file.write(res.text)

    tree = ET.parse('cur.xml')
    root = tree.getroot()

    for ch in root.findall('Valute'):
        if ch.find('NumCode').text == '840':
            value = ch.find('Value').text
            return value

    return None

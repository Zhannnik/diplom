# Жанна Моисеева, 34-я когорта — Финальный проект. Инженер по тестированию плюс
# Импорт необходимых модулей и данных для запроса
import configuration
import requests
import data


# Создаем заказ
# Определение функции для отправки POST запроса на создание заказа
def post_order(order_body):
    return requests.post(
        configuration.URL_SERVICE + configuration.CREATE_ORDERS_PATH,
        json=order_body,
        headers={"Content-Type": "application/json"},
    )


# Определение функции для отправки GET запроса на получение заказа по трек-номеру
def get_order_from_track(track):
    return requests.get(
        configuration.URL_SERVICE + configuration.FIND_ORDER_PATH + str(track),
        headers={"Content-Type": "application/json"},
    )

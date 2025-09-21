import configuration
import requests
import data


# Создаем заказ
def post_order(order_body):
    return requests.post(
        configuration.URL_SERVICE + configuration.CREATE_ORDERS,
        json=order_body,
        headers=data.headers,
    )


# Получаем заказ по трек-номеру
def get_order_from_track(track):
    return requests.get(
        configuration.URL_SERVICE + configuration.FIND_ORDER + str(track),
        headers=data.headers,
    )

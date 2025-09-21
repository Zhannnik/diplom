import configuration
import requests
import data


# Создаем заказ
def post_order(order_body):
    print(order_body)
    return requests.post(
        configuration.URL_SERVICE + configuration.CREATE_ORDERS,
        json=order_body,
        headers=data.headers,
    )


response = post_order(data.order_body)
print(response.status_code)


# Получаем трек-номер
def get_order_from_track(track):
    return requests.get(
        configuration.URL_SERVICE + configuration.FIND_ORDER + str(track),
        headers=data.headers,
    )


# Получаем заказ по трек-номеру
def assertion_code_200():
    response_pno = post_order(data.order_body)
    track = response_pno.json()["track"]
    print("----------")
    print(track)
    print("___________")
    order_response = get_order_from_track(track)
    assert order_response.status_code == data.status_code_200, "Код не 200"
    return order_response

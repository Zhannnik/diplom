# Жанна Моисеева, 34-я когорта — Финальный проект. Инженер по тестированию плюс
# Импортируем модуль sender_stand_request, содержащий функции для отправки HTTP-запросов к API.
import sender_stand_request

# Импортируем модуль data, в котором определены данные, необходимые для HTTP-запросов.
import data


# тест статус 200
def test_order_info_code_200():
    # Делаем POST запрос на создание заказа c использованием функции post_order из модуля sender_stand_request
    # В качестве параметров используются данные order_body из модуля data
    # Результат вызова сохраняем в переменную response_pno
    response_pno = sender_stand_request.post_order(data.order_body)
    # в переменную track сохраняется трек-номер заказа, извлеченный из JSON-ответа сервера после выполнения запроса на создание заказа.
    track = response_pno.json()["track"]
    # Делаем GET запрос на получение заказа c использованием функции get_order_from_track из модуля sender_stand_request
    # В качестве параметра используется ранее сохраненный трек-номер заказа в переменную track
    # Результат вызова сохраняем в переменную order_response
    order_response = sender_stand_request.get_order_from_track(track)
    # Проверяем код ответа в результате вызова order_response, если код ответа не 200 - выводим ошибку "Код не 200"
    assert order_response.status_code == 200, "Код не 200"

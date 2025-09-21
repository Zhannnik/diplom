import sender_stand_request
import data


# тест статус 200
def test_order_info_code_200():
    response_pno = sender_stand_request.post_order(data.order_body)
    track = response_pno.json()["track"]
    order_response = sender_stand_request.get_order_from_track(track)
    print(order_response.json())
    assert order_response.status_code == data.status_code_200, "Код не 200"

from fastapi.testclient import TestClient

from app.main import app, startup_event


startup_event()
client = TestClient(app)


def test_zero_equation():
    response = client.post("/equation/", json={"a": 0, "b": 0, "c": 0})
    assert response.status_code == 422
    assert response.json() == {"result": "division by zero"}


def test_no_answers():
    response = client.post("/equation/", json={"a": 1, "b": 1, "c": 1})
    assert response.status_code == 200
    assert response.json() == {"result": "Уравнение не имеет корней"}


def test_one_answer():
    response = client.post("/equation/", json={"a": -4, "b": 28, "c": -49})
    assert response.status_code == 200
    assert response.json() == {"result": "Корень уравнения x = 3.5"}


def test_two_answers():
    response = client.post("/equation/", json={"a": 4, "b": 5, "c": 1})
    assert response.status_code == 200
    assert response.json() == {"result": "Корни уравления x = -0.25, -1.0"}


def test_get_color():
    response = client.get("/color/12")
    assert response.status_code == 200
    assert response.json() == {"result": response.json()["result"]}


def test_get_color_not_found():
    response = client.get("/color/200")
    assert response.status_code == 404

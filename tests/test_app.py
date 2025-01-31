from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_app.app import app


def test_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)

    response = client.get('/')

    assert response.status_code == HTTPStatus.OK  # assert
    assert response.json() == {'message': 'Olá, bem-vindo ao FastAPI!'}

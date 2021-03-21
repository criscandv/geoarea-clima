from flask import json
from app import app
from config import TestingConfig as Config


app.config.from_object(Config)


def decode_data(data):
    return json.loads(data.decode('utf8'))


def test_api_data():
    response = app.test_client().get('/')
    assert response.status_code == 200


def test_clima_data():
    response = app.test_client().get('/get-clima-data/')
    data = decode_data(response.data)
    assert response.status_code == 200
    assert data['len_results'] == 14

    # Query param
    response = app.test_client().get('/get-clima-data/?localidad=Mad')
    data = decode_data(response.data)
    assert response.status_code == 200
    assert data['len_results'] == 7

    # Not found
    response = app.test_client().get('/get-clima-data/?localidad=Vasco')
    data = decode_data(response.data)
    assert response.status_code == 200
    assert data['len_results'] == 0

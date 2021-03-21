import os
import requests

from flask import Flask
from flask import request
from flask import jsonify
from flask import Response
from flask_sqlalchemy import SQLAlchemy

from config import DevelopmentConfig as Config
from external_requests import get_weather_data

app = Flask(__name__)
app.config.from_object(Config)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import *


def insert_days(data):
    for i in range(7):
        day = data[f'day{i+1}']
        day['city'] = data['locality'].get('name')
        day_model = Day(**day)
        db.session.add(day_model)
        db.session.commit()


def insert_hour(data, localidad):
    for i in data:
        hour = data[i]
        day = Day.query.filter_by(date=hour['date'], city=localidad).first()
        hour['day_id'] = day.id
        hour_model = Hour(**hour)
        db.session.add(hour_model)
        db.session.commit()


@app.route('/')
def get_api_data():
    """
    Get data from external url an set into database
    :return: Api url to get the data from database
    """
    try:
        lang = request.args.get('lang', 'es')
        climate_madrid = get_weather_data(lang, 3768)
        climate_bcn = get_weather_data(lang, 7183)

        if not climate_madrid['status_code'] == 200 or not climate_bcn['status_code'] == 200:
            raise Exception('Error al obtener los datos de la api externa')

        insert_days(climate_madrid['response'])
        insert_hour(climate_madrid['response'].get('hour_hour'), 'Madrid')

        insert_days(climate_bcn['response'])
        insert_hour(climate_bcn['response'].get('hour_hour'), 'Barcelona')

        return 'Database updated. <br><a href="http://localhost:5000/get-clima-data/" target="_blank">Check this route to see the data</a>'

    except Exception as e:
        return Response(e, status=500)


@app.route('/get-clima-data/')
def get_clima_data():
    return 'Return data'


if __name__ == '__main__':
    app.run()

import os
import requests

from flask import Flask
from flask import request
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy

from .config import DevelopmentConfig as Config
from .external_requests import get_weather_data


app = Flask(__name__)
app.config.from_object(Config)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route('/')
def get_api_data():
    """
    Get data from external url an set into database
    :return: Api url to get the data from database
    """
    lang = request.args.get('lang', 'es')
    climate = get_weather_data(lang)
    print("\n\n\n")
    print("climate ", climate['status_code'])
    print("\n\n\n")

    # return 'Database updated. <br><a href="http://localhost:5000/get-clima-data/" target="_blank">Check this route to see the data</a>'
    return jsonify(
        response=climate['response'],
        status=200
    )


@app.route('/get-clima-data/')
def get_clima_data():
    return 'Return data'


if __name__ == '__main__':
    app.run()

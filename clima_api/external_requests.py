import requests
from .config import Config


def get_weather_data(lang):
    localidad = 7087
    req = requests.get(f'https://api.tutiempo.net/json/?lan={lang}&apid={Config.CLIMATE_API_KEY}&lid={localidad}')

    return {
        "response": req.json(),
        "status_code": req.status_code
    }

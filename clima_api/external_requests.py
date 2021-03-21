import requests
from config import Config


def get_weather_data(lang, localidad):
    try:
        # Bcn = 7183
        # Madrid = 3768
        req = requests.get(f'https://api.tutiempo.net/json/?lan={lang}&apid={Config.CLIMATE_API_KEY}&lid={localidad}')

        return {
            "response": req.json(),
            "status_code": req.status_code
        }

    except Exception as e:
        return e
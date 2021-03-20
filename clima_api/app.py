from flask import Flask
from .config import DevelopmentConfig


app = Flask(__name__)
app.config.from_object(DevelopmentConfig)


@app.route('/')
def hello_world():
    return 'Dockerizando flask'


@app.route('/get-clima-data')
def get_clima_data():
    return 'Set data into databasee'


if __name__ == '__main__':
    app.run()

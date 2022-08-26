from flask import Flask, jsonify
from weather_forecast_controller import WeatherForecastController
app = Flask(__name__)


@app.route('/')
def index():
    return 'Server running.'


@app.route('/forecast')
def get_forecast():
    forecast = WeatherForecastController().get(5)
    return jsonify(forecast)

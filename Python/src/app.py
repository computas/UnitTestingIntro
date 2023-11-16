from datetime import date, timedelta
from random import choice, randint
from flask import Flask
from weather_forecast import WeatherForecast, WeatherForecastDay, possible_summaries

app = Flask(__name__)


@app.route('/')
def index():
    return 'Server running.'


@app.route('/forecast')
def get_forecast():
    days = [
        WeatherForecastDay(
            date = date.today() + timedelta(days = i),
            temperature_c = randint(-20, 55),
            summary = choice(possible_summaries)
        )
        for i in range(5)
    ]
    return WeatherForecast(forecast=days).model_dump_json()

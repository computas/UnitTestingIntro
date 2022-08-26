from weather_forecast import WeatherForecast
from datetime import datetime, timedelta
from random import choice, randint
from typing import List


class WeatherForecastController:
    @property
    def summaries(self) -> List[str]:
        return ["Freezing", "Bracing", "Chilly", "Cool", "Mild",
                "Warm", "Balmy", "Hot", "Sweltering", "Scorching"]

    def get(self, days) -> str:
        return [
            WeatherForecast(
                date = datetime.now() + timedelta(days = i),
                temperature_c = randint(-20, 55),
                summary = choice(self.summaries)
            )
            for i in range(days)
        ]

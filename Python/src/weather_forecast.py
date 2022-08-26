import datetime
from temperature import convert_c_to_f


class WeatherForecast(dict):
    def __init__(self, date: datetime, temperature_c: int, summary: str):
        dict.__init__(
            self, date=date,
            temperature_c=temperature_c,
            temperature_f=int(convert_c_to_f(temperature_c)),
            summary=summary
        )

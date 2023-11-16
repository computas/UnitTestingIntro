from datetime import date
from pydantic import BaseModel, computed_field
from temperature import convert_c_to_f

class WeatherForecastDay(BaseModel):
    date: date
    temperature_c: float
    summary: str
    
    @computed_field
    @property
    def temperature_f(self) -> float:
        return convert_c_to_f(self.temperature_c)


class WeatherForecast(BaseModel):
    forecast: list[WeatherForecastDay]


possible_summaries = [
    "Freezing", "Bracing", "Chilly", "Cool", "Mild",
    "Warm", "Balmy", "Hot", "Sweltering", "Scorching"
]

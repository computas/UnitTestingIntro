namespace ProductionCode;

public class WeatherForecast
{
    public DateTime Date { get; set; }

    public int TemperatureC { get; set; }

    public int TemperatureF
    {
        get
        {
            var mattulator = new Mattulator();
            var sum = mattulator.Adder(32, (int) (TemperatureC / 0.5556));
            return (int)sum;
        }
    }

    public string? Summary { get; set; }
}
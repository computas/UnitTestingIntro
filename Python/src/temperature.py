from mattulator import Mattulator


def convert_c_to_f(temperature_c: float) -> float:
    div = Mattulator.divide(temperature_c, 0.5556)
    return Mattulator.add(32, div)


def convert_f_to_c(temperature_f: float) -> float:
    sub = Mattulator.subtract(temperature_f, 32)
    return Mattulator.multiply(sub, 0.5556)

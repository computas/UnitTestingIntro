from mattulator import Mattulator


def convert_c_to_f(temperature_c: float) -> float:
    res = Mattulator.divide(temperature_c, 5)
    res = Mattulator.multiply(res, 9)
    return Mattulator.add(32, res)


def convert_f_to_c(temperature_f: float) -> float:
    res = Mattulator.subtract(temperature_f, 32)
    res = Mattulator.divide(res, 9)
    return Mattulator.multiply(res, 5)

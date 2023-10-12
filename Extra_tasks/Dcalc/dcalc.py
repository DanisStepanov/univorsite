from math import pi
from typing import Union
def deg_to_gms(deg: float, formats: str ='string') -> Union[int, float]:
    degrees = int(deg)
    minutes = int((deg - degrees) * 60)
    seconds = ((((deg - degrees) * 60) - minutes) * 60)
    seconds = round(seconds, 5)

    if formats == 'string':
        answer = f'{degrees}° {minutes}′ {seconds}″'
    elif formats == 'num':
        answer = (degrees, minutes, seconds)
    else:
        answer = None
    return answer
def gms_to_deg(degrees: int, minutes: int, seconds: Union[int, float]) -> float:
    return degrees + (minutes / 60) + (seconds / 3600)
def deg_to_rad(deg: float) -> float:
    return deg * (pi / 180)
def rad_to_deg(rad: float) -> float:
    return rad * (180 / pi)
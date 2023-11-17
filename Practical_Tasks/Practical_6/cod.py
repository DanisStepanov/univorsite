import re

def add_data(a):
    text=re.compile("Рейс (\d+) (отправился|прибыл) (из|в) (\w+) в (\d+):(\d+):(\d+)")
    for m in text.finditer(a):
        newtext = text.sub(fix_date, a)
        return newtext

def fix_date(m):
    return f"[{m.group(5)}:{m.group(6)}:{m.group(7)}] - Поезд № {m.group(1)} {m.group(3)} {m.group(4)} "

file = open('info.txt', mode='r', encoding='utf-8')

def new_f(file):
    info = file.read().splitlines()
    with open("new.txt", mode="w", encoding="utf8") as new:
        new.write('')
    for string in info:
        new_format = (add_data(string))
        if new_format != None:
            with open("new.txt", mode="a", encoding="utf8") as new_flights:
                new_flights.write(f"{ add_data(string)}\n")

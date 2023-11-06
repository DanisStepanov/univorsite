from paradox import *
def show():
    a =int(input('Введите количество монте-итераций: '))
    print(monty_hall(int(a)), "%")
    c=int(input('Количество итераций групп: '))
    b = int(input('Введите количество человек в группе: '))
    print(birthday(int(b),c), "%")
if __name__ == "__main__":
    show()
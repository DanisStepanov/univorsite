from Practical_Tasks.Practical_7.cod import *

def show():
    while True:
        try:
            print('Для выхода нажмите 0')
            input_user = input("Введите название книги: ")
            if input_user == '0':
                print('Вы вышли из поиска книги!')
                break
            data = get_books(input_user)
            print(data)
            print(get_totals(data))
        except:
            print('')
if __name__ == "__main__":
    show()
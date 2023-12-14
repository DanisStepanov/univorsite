import os
def main():
    try:
        name = input('Введите имя файла, для его будущего использования:')
        if not os.path.exists(f"{name}.txt"):
            flag=False
            while flag == False:
                name = input('Такого файла нет, попробуйте ещё раз: ').strip()
                if os.path.exists(f"{name}.txt"):
                    flag = True
        open_file = open(f"{name}.txt")
        read = int(open_file.readline())
        a = [int(x) for x in open_file.readlines()]
        open_file.close()
        return a
    except FileNotFoundError:
        print("Такого файла нет, попробуйте ещё раз: ")
    except OSError:
        return "Ошибка операционной системы!"
    except ValueError:
        return "В файле есть специфические символы!"
    except :
        return "Произошла фотальная ошибка!"
    else:
        return main()

####Прописать все ошибки до конца и в конце фотальная ошибка
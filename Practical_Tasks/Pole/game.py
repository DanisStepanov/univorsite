from random import randint
def get_words():
    with open("words.txt", mode="r", encoding="utf8") as f:
        words = f.read().splitlines()
    return words
def interface():
    while True:
        level = input("Введите уровень сложности:"
                      "\n1 - Новичок."
                      "\n2 - Средничок."
                      "\n3 - Старый.\n")
        if level == '1':
            default_health = 10
            break
        elif level == '2':
            default_health = 5
            break
        elif level == '3':
            default_health = 3
            break
        else:
            print("Вы ввели неправильное значение!")

    health = default_health

    return default_health,health
def game(default_health:int,health:int):
    letter = ""
    words = get_words()
    file_record = get_record()
    record = 0
    word = words[randint(0, len(words) - 1)]
    word_hide = []

    for i in range(0, len(word)):
        word_hide.append("*")

    playing = True


    while playing !=False:
        if "".join(word_hide) != word.upper() and health > 0:
            word_hide_str = " ".join(word_hide)
            print(f"{word_hide_str}  количество жизней {health}")
            letter = input("Назовите букву или слово целиком: ")

        if letter.upper() == word.upper() or "".join(word_hide) == word.upper():
            record += 1
            words.remove(word)
            print(" ".join(word.upper()))
            print("Вы выиграли")
            print(f"Ваш рекорд: {max(record, file_record)}")

            if len(words) == 0:
                print("Все слова угаданы.")
                break

            elif input("Вы хотите продолжить Введите 1-если да 0-если нет? ") == "1":
                playing=True
                health = default_health
                word = words[randint(0, len(words) - 1)]
                word_hide = ["*" for _ in range(len(word))]
            else:
                print('Хорошего дня')
                break
        elif letter.upper() in word_hide:
            print("Такая буква уже есть.")
            health-=1
        elif letter.upper() not in word.upper() and len(letter) > 1:
            health = 0
        elif letter in word:
            if letter.upper() not in word_hide:
                for i in range(0, len(word)):
                    if word[i] == letter:
                        word_hide[i] = letter.upper()
        elif letter.lower() in word and len(letter) == 1 and not letter.upper() in ''.join(word_hide):
                for i in range(len(word)):
                    if word[i] == letter.lower():
                        word_hide[i] = letter.upper()
                print(f"Откройте букву: '{letter.upper()}'")
        if health == 0:
            if input("Хотите восстановить жизни? Введите 1-если да 0-если нет\n") == "1":
                print(f"Рекорд: {max(record, file_record)}")
                health = default_health
            else:
                print('Хорошего дня')
                break
        elif not letter.lower() in word:
            health -= 1
            print(f"Такой буквы нет в слове. Вы теряете жизнь.")

    save_record(max(record, file_record))


def get_record():
    with open("rec.txt", mode="r", encoding="utf8") as f:
        file_record = int(str(f.read()))
    return file_record


def save_record(record: int):
    with open("rec.txt", mode="w", encoding="utf8") as file:
        file.write(str(record))

if __name__ == "__main__":
    default_health, health = interface()
    game(default_health, health)
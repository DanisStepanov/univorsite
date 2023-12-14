import csv

def get_books(word: str):
    file = open("books.csv", mode="r", encoding="utf-8")
    string = csv.reader(file, delimiter='|')
    print(string)
    spisok = []
    for row in string:
        if word.lower() in row[1].lower():
            spisok.append(row)
    return spisok


def get_totals(data: list, add=100):
    spisok = []
    for row in data:
        #print(row)
        if not (str(row[3]).isdigit() or str(row[4]).isdigit()):
            continue
        if (int(row[3]) * float(row[4])) < 500:
            spisok.append((row[0], int(row[3]) * float(row[4]) + add))
        else:
            spisok.append((row[0], int(row[3]) * float(row[4])))
    return spisok


if __name__ == "__main__":
    file = open("books.csv", "r", encoding="utf-8")
    reader = csv.reader(file, delimiter='|')
    book = get_books("python")
    print(book)
    print(get_totals(book))
    print(get_totals(list(reader)))

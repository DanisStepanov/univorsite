def read_file(name):
    text_fail = open("data.txt", mode="r", encoding="utf8")
    text = text_fail.read().splitlines()
    string_list = [text[i].split(' ') for i in range(len(text))]
    uniue = []
    for i in range(len(string_list)):
        for word in string_list[i]:
            word = ''.join(filter(str.isalnum, word)).lower()
            if len(word) > 0:
                uniue.append(word)
    words_set = set(uniue)
    return sorted(words_set)

words = read_file('data.txt')

def save_file(name, words):
    new_text = open(f"{name}", mode='w', encoding='utf8')
    new_text.write(f"{(len(words))} \n")
    for i in range(len(words)):
        new_text.write(f"{(words[i])} \n")

save_file('new.txt', words)
'''6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом. Каждое слово состоит
 из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
 Необходимо использовать написанную ранее функцию int_func().'''

def str_check(str_check: str) -> bool:

    for char in str_of_words:
        char_code = ord(char)
    if ((((char_code != 35) and (char_code < 97))) or (char_code > 122)):
        check = False
    else:
        check = True
    return check


def word_first_letter_up(word: str) -> str:
    s = chr(ord(word[0]) - 32)
    return s + word[1:]


while True:
    str_of_words = input('Введите строку слов из латинских букв в нижнем регистре, разделенных пробелами: ')

    if str_check(str_of_words):
        break
    else:
        print("Не верное значение данных\n")
        continue


list_of_word = str_of_words.split()
str_of_words = ''
for word in list_of_word:
    str_of_words = str_of_words + word_first_letter_up(word) + ' '
    
print(str_of_words)
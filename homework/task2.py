'''
2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
'''

word_str_list = []

with open("To_task2", 'r') as file:
    for idx, line in enumerate(file):
        word_str_list.append([idx + 1, len(line.split())])
        print(f'В строке {word_str_list[idx][0]} слов {word_str_list[idx][1]}')


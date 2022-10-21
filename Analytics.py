import multiprocessing
from multiprocessing import Process
from random import randint
from typing import List
from RandomWordGenerator import RandomWord
import os

def length_file(name_file):
    file = open(name_file, 'r')
    l = 0
    for line in file:
        l += 1
    file.close()
    return l
#Всего символов
def total(name_file: str):
    file = open(name_file, 'r')
    t = 0
    for line in file:
        for word in line:
            if word != '\n':
                t += len(word)
    file.close()
    return t
#Максимальная длина
def max_length(name_file: str):
    file = open(name_file, 'r')
    list_file: List[str] = file.read().split()
    maxlen: int = len(list_file[0])
    for line in list_file:
        if maxlen < len(line):
            maxlen = len(line)
    file.close()
    return maxlen
#Минимальная длина
def min_length(name_file: str):
    file = open(name_file, 'r')
    list_file: List[str] = file.read().split()
    minlen: int = len(list_file[0])
    for line in list_file:
        if minlen > len(line):
            minlen = len(line)
    file.close()
    return minlen
#Средняя длина
def mid_length(name_file: str):
    midlen: int = total(name_file) / length_file(name_file)
    return midlen
#Счет гласных букв
def vowel(name_file: str):
    file = open(name_file, 'r')
    vow: int = 0
    for line in file:
        for ch in line:
            if ch in ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']:
                vow += 1
            else:
                pass
    file.close()
    return vow
#Счет согласных букв
def consonant(name_file: str):
    file = open(name_file, 'r')
    consonant: int = 0
    for line in file:
        for ch in line:
            if ch in ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y', '\n', ' ']:
                pass
            else:
                consonant += 1
    file.close()
    return consonant
#Счет повторений слов с одинаковой длиной
def repetitions(name_file: str):
    file = open(name_file, 'r')
    list_file: List[str] = file.read().split()
    rep_dict: dict = dict()
    # Создание словаря с повторениями
    for word in list_file:
        if len(word) in rep_dict:
            rep_dict[len(word)] += 1
        else:
            rep_dict[len(word)] = 1
    # Сортировка словаря с повторениями
    sorted_dict = {}
    sorted_keys = sorted(rep_dict.keys())

    for w in sorted_keys:
        sorted_dict[w] = rep_dict[w]
    rep_dict = sorted_dict.copy()
    #Строка для вывода повторений
    rep: str = ""
    for key in rep_dict:
        rep += f"   * {key} сим. >> {rep_dict[key]} повторений.\n"
    file.close()
    return rep
# Аналитика файла
def analytics(name_file: str):
    # Вывод
    t:str = ""
    for i in range(55):
        t += '*'

    print(t + f"\n" + f"Аналитика для файла {name_file}" + f"\n" + t + f"\n" +
          f"1. Всего символов --> {total(name_file)}\n" +
          f"2. Максимальная длина слова --> {max_length(name_file)}\n" +
          f"3. Минимальная длина слова --> {min_length(name_file)}\n" +
          f"4. Средняя длина слова --> {mid_length(name_file)}\n" +
          f"5. Количество гласных --> {vowel(name_file)}\n" +
          f"6. Количество согласных --> {consonant(name_file)}\n" +
          "7. Количество повторений слов с одинаковой длиной:\n"+
          f"{repetitions(name_file)} \n")


name_file: str = f'./result_files/Process-{1}-.txt'
analytics(name_file)
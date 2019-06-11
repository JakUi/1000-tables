#!/usr/bin/env python
# coding: utf-8

# In[1]:


from IPython.core.display import display, HTML
import csv
import os
import shutil
import random
from threading import Thread
display(HTML("<style>.container { width:90% !important; }</style>")) #здесь можно задать ширину ячейки в % ширины экрана


# In[3]:


csv_list =[]
b1, b2, b3, b4 = [], [], [], []
b5, b6, b7, b8 = [], [], [], []
def get_files(csv_list):
    #!!!!!!!!!!!!!!!!!!!!!!!!!
    tree = os.listdir('C:\\Users\\Aleksandr\\Jupyter projects\\n test') #Здесь нужно прописать твой путь!!!!
    
    #обавим все имена файлов, с раширением .csv в нашей папке в список 
    for tr in tree:
        if tr.count('.csv') == True: #если в имени файла есть .csv
            csv_list.append(tr) #добавляем имя в список файлов для обработки
    return csv_list
#предположим, что у нас 8-поточный ЦП тогда будем обрабатывать таблицы параллельно в 8-ми потоках

def exec_1(csv_list, b1): #будет обрабатывать первые 125 таблиц
    #читаем каждый файл из списка, его элементы переносим в список а
    a = []
    for k in range(0, 124):
        csv_path = csv_list[k]
        with open(csv_path, "r") as f_obj:
            reader = csv.reader(f_obj)
            for row in reader:
                a.append(row) #каждую строку таблицы добавляем в список a              
    for x in range(0, len(a)): #проходим по всей таблице (она сейчас в списке)
        for y in range(0, len(a[x])):
            a[x][y] = a[x][y].replace('"', '') #меняем двоеточие на пробел (разбиваем числа на пары)
            a[x][y] = a[x][y].replace(':', ' ') #меняем двоеточие на пробел (разбиваем числа на пары)
            a[x][y] = a[x][y].replace(',', '') #избавляемся от запятой между парами чисел
            a[x][y] = a[x][y].split() #строку чисел на отдельное число в строке
    #сейчас a это многомерный массив из списков со строками внутри, чтобы сделать его списком нужен доп список :(
            for elem in a[x][y]: #каждую строку в каждом элементе-списке списка а
                b1.append(float(elem)) #преобразуем в число c плавающей запятой и добавляем в спиок b
   # print(len(b1)) #убери решетку перед принт, если хочшь узнать кол-во элементов в массиве)
    #print(b1[0:100000])
    return b1
def exec_2(csv_list, b2):
    #читаем каждый файл из списка, его элементы переносим в список а
    a, b2 = [], []
    for k in range(125, 249):
        csv_path = csv_list[k]
        with open(csv_path, "r") as f_obj:
            reader = csv.reader(f_obj)
            for row in reader:
                a.append(row) #каждую строку таблицы добавляем в список a              
    for x in range(0, len(a)): #проходим по всей таблице (она сейчас в списке)
        for y in range(0, len(a[x])):
            a[x][y] = a[x][y].replace('"', '') #меняем двоеточие на пробел (разбиваем числа на пары)
            a[x][y] = a[x][y].replace(':', ' ') #меняем двоеточие на пробел (разбиваем числа на пары)
            a[x][y] = a[x][y].replace(',', '') #избавляемся от запятой между парами чисел
            a[x][y] = a[x][y].split() #строку чисел на отдельное число в строке
    #сейчас a это многомерный массив из списков со строками внутри, чтобы сделать его списком нужен доп список :(
            for elem in a[x][y]: #каждую строку в каждом элементе-списке списка а
                b2.append(float(elem)) #преобразуем в число c плавающей запятой и добавляем в спиок b
    #print(len(b2)) #убери решетку перед принт, если хочшь узнать кол-во элементов в массиве)
    #print(b2[0:100000])
    return b2
def exec_3(csv_list, b3): 
    #читаем каждый файл из списка, его элементы переносим в список а
    a, b3 = [], []
    for k in range(250, 374):
        csv_path = csv_list[k]
        with open(csv_path, "r") as f_obj:
            reader = csv.reader(f_obj)
            for row in reader:
                a.append(row) #каждую строку таблицы добавляем в список a              
    for x in range(0, len(a)): #проходим по всей таблице (она сейчас в списке)
        for y in range(0, len(a[x])):
            a[x][y] = a[x][y].replace('"', '') #меняем двоеточие на пробел (разбиваем числа на пары)
            a[x][y] = a[x][y].replace(':', ' ') #меняем двоеточие на пробел (разбиваем числа на пары)
            a[x][y] = a[x][y].replace(',', '') #избавляемся от запятой между парами чисел
            a[x][y] = a[x][y].split() #строку чисел на отдельное число в строке
    #сейчас a это многомерный массив из списков со строками внутри, чтобы сделать его списком нужен доп список :(
            for elem in a[x][y]: #каждую строку в каждом элементе-списке списка а
                b3.append(float(elem)) #преобразуем в число c плавающей запятой и добавляем в спиок b
    #print(len(b3)) #убери решетку перед принт, если хочшь узнать кол-во элементов в массиве)
    #print(b3[0:100000])
    return b3
def exec_4(csv_list, b4):
    #читаем каждый файл из списка, его элементы переносим в список а
    a, b4 = [], []
    for k in range(375, 500):
        csv_path = csv_list[k]
        with open(csv_path, "r") as f_obj:
            reader = csv.reader(f_obj)
            for row in reader:
                a.append(row) #каждую строку таблицы добавляем в список a              
    for x in range(0, len(a)): #проходим по всей таблице (она сейчас в списке)
        for y in range(0, len(a[x])):
            a[x][y] = a[x][y].replace('"', '') #меняем двоеточие на пробел (разбиваем числа на пары)
            a[x][y] = a[x][y].replace(':', ' ') #меняем двоеточие на пробел (разбиваем числа на пары)
            a[x][y] = a[x][y].replace(',', '') #избавляемся от запятой между парами чисел
            a[x][y] = a[x][y].split() #строку чисел на отдельное число в строке
    #сейчас a это многомерный массив из списков со строками внутри, чтобы сделать его списком нужен доп список :(
            for elem in a[x][y]: #каждую строку в каждом элементе-списке списка а
                b4.append(float(elem)) #преобразуем в число c плавающей запятой и добавляем в спиок b
    #print(len(b4)) #убери решетку перед принт, если хочшь узнать кол-во элементов в массиве)
    #print(b4[0:100000])
    return b4
def exec_5(csv_list, b5):
    #читаем каждый файл из списка, его элементы переносим в список а
    a, b5 = [], []
    for k in range(501, 625):
        csv_path = csv_list[k]
        with open(csv_path, "r") as f_obj:
            reader = csv.reader(f_obj)
            for row in reader:
                a.append(row) #каждую строку таблицы добавляем в список a              
    for x in range(0, len(a)): #проходим по всей таблице (она сейчас в списке)
        for y in range(0, len(a[x])):
            a[x][y] = a[x][y].replace('"', '') #меняем двоеточие на пробел (разбиваем числа на пары)
            a[x][y] = a[x][y].replace(':', ' ') #меняем двоеточие на пробел (разбиваем числа на пары)
            a[x][y] = a[x][y].replace(',', '') #избавляемся от запятой между парами чисел
            a[x][y] = a[x][y].split() #строку чисел на отдельное число в строке
    #сейчас a это многомерный массив из списков со строками внутри, чтобы сделать его списком нужен доп список :(
            for elem in a[x][y]: #каждую строку в каждом элементе-списке списка а
                b5.append(float(elem)) #преобразуем в число c плавающей запятой и добавляем в спиок b
    #print(len(b5)) #убери решетку перед принт, если хочшь узнать кол-во элементов в массиве)
    #print(b5[0:100000])
    return b5
def exec_6(csv_list, b6):
    #читаем каждый файл из списка, его элементы переносим в список а
    a, b6 = [], []
    for k in range(626, 750):
        csv_path = csv_list[k]
        with open(csv_path, "r") as f_obj:
            reader = csv.reader(f_obj)
            for row in reader:
                a.append(row) #каждую строку таблицы добавляем в список a              
    for x in range(0, len(a)): #проходим по всей таблице (она сейчас в списке)
        for y in range(0, len(a[x])):
            a[x][y] = a[x][y].replace('"', '') #меняем двоеточие на пробел (разбиваем числа на пары)
            a[x][y] = a[x][y].replace(':', ' ') #меняем двоеточие на пробел (разбиваем числа на пары)
            a[x][y] = a[x][y].replace(',', '') #избавляемся от запятой между парами чисел
            a[x][y] = a[x][y].split() #строку чисел на отдельное число в строке
    #сейчас a это многомерный массив из списков со строками внутри, чтобы сделать его списком нужен доп список :(
            for elem in a[x][y]: #каждую строку в каждом элементе-списке списка а
                b6.append(float(elem)) #преобразуем в число c плавающей запятой и добавляем в спиок b
    #print(len(b6)) #убери решетку перед принт, если хочшь узнать кол-во элементов в массиве)
    #print(b6[0:100000])
    return b6
def exec_7(csv_list, b7): 
    #читаем каждый файл из списка, его элементы переносим в список а
    a, b7 = [], []
    for k in range(751, 875):
        csv_path = csv_list[k]
        with open(csv_path, "r") as f_obj:
            reader = csv.reader(f_obj)
            for row in reader:
                a.append(row) #каждую строку таблицы добавляем в список a              
    for x in range(0, len(a)): #проходим по всей таблице (она сейчас в списке)
        for y in range(0, len(a[x])):
            a[x][y] = a[x][y].replace('"', '') #меняем двоеточие на пробел (разбиваем числа на пары)
            a[x][y] = a[x][y].replace(':', ' ') #меняем двоеточие на пробел (разбиваем числа на пары)
            a[x][y] = a[x][y].replace(',', '') #избавляемся от запятой между парами чисел
            a[x][y] = a[x][y].split() #строку чисел на отдельное число в строке
    #сейчас a это многомерный массив из списков со строками внутри, чтобы сделать его списком нужен доп список :(
            for elem in a[x][y]: #каждую строку в каждом элементе-списке списка а
                b7.append(float(elem)) #преобразуем в число c плавающей запятой и добавляем в спиок b
    #print(len(b7)) #убери решетку перед принт, если хочшь узнать кол-во элементов в массиве)
    #print(b7[0:100000])
    return b7
def exec_8(csv_list, b8): 
    #читаем каждый файл из списка, его элементы переносим в список а
    a, b8 = [], []
    for k in range(876, len(csv_list)):
        csv_path = csv_list[k]
        with open(csv_path, "r") as f_obj:
            reader = csv.reader(f_obj)
            for row in reader:
                a.append(row) #каждую строку таблицы добавляем в список a              
    for x in range(0, len(a)): #проходим по всей таблице (она сейчас в списке)
        for y in range(0, len(a[x])):
            a[x][y] = a[x][y].replace('"', '') #меняем двоеточие на пробел (разбиваем числа на пары)
            a[x][y] = a[x][y].replace(':', ' ') #меняем двоеточие на пробел (разбиваем числа на пары)
            a[x][y] = a[x][y].replace(',', '') #избавляемся от запятой между парами чисел
            a[x][y] = a[x][y].split() #строку чисел на отдельное число в строке
    #сейчас a это многомерный массив из списков со строками внутри, чтобы сделать его списком нужен доп список :(
            for elem in a[x][y]: #каждую строку в каждом элементе-списке списка а
                b8.append(float(elem)) #преобразуем в число c плавающей запятой и добавляем в спиок b
    #print(len(b8)) #убери решетку перед принт, если хочшь узнать кол-во элементов в массиве)
    #print(b8[0:100000])
    return b8
get_files(csv_list)
#print(csv_list)
thread1 = Thread(target = exec_1, args = (csv_list, b1,))
thread2 = Thread(target = exec_2, args = (csv_list, b2,))
thread3 = Thread(target = exec_3, args = (csv_list, b3,))
thread4 = Thread(target = exec_4, args = (csv_list, b4,))
thread5 = Thread(target = exec_5, args = (csv_list, b5,))
thread6 = Thread(target = exec_6, args = (csv_list, b6,))
thread7 = Thread(target = exec_7, args = (csv_list, b7,))
thread8 = Thread(target = exec_8, args = (csv_list, b8,))
thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()
thread6.start()
thread7.start()
thread8.start()
thread1.join()
thread2.join()
thread3.join()
thread4.join()
thread5.join()
thread6.join()
thread7.join()
thread8.join()
bb = b1 + b2 + b3 + b4 + b5 + b6 + b7 + b8 #это будет список, который тебе нужен (который ты хочешь подать на вход нейронки)
print(len(bb))
batch = open('batch.txt', 'w')
batch.write(str(bb))
batch.close()


# In[ ]:





# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между
# максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from math import trunc

floatlist = [1.1, 1.2, 3.1, 5, 10.01]
templist = []
for i in range(len(floatlist)):
    templist.append(floatlist[i] - int(floatlist[i]))
resultat = max(templist)-min(templist)
print(trunc(resultat*100)/100)

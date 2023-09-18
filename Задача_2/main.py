# Задача 32:
# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)


from random import randint
list_1=[randint(1, 10) for i in range(10)]
print(list_1)
List_2=[]
max=8
min=3
for i in range(len(list_1)):
     if list_1[i]>=min and list_1[i]<=max:
      List_2.append(i)
      print(List_2)
        

        

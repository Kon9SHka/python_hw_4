#   Задача 22:
# Даны два неупорядоченных набора целых чисел (может быть, с
#  повторениями). Выдать без повторений в порядке возрастания все те числа, которые
#  встречаются в обоих наборах.
#  Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
#  элементов второго множества. Затем пользователь вводит сами элементы множеств.

def fill_list(cnt):
    i = 0
    lst = []
    while i < cnt:
        lst.append(int(input("Введите "+str(i+1)+" число: ")))
        i+=1
    return lst
        

n = int(input("Введите кол-во чисел в первом массиве: "))
m = int(input("Введите кол-во чисел во втором массиве: "))

first_array = fill_list(n)
second_array = fill_list(m)

print(first_array)
print(second_array)

print(set(first_array) & set(second_array))


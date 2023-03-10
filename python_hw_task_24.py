#   Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# i ягод.
#    Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
#  выросло различное число ягод – на i-ом кусте выросло a
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.
import random

n = int(input("Введите кол-во кустов: "))
gryadka = []
for i in range(0,n):
    gryadka.append(random.randint(0,32))
    i+=1
    
max_sum_yagod = 0

for i in range(1, len(gryadka)-1):
    current_sum = gryadka[i-1]+gryadka[i]+gryadka[i+1]
    if current_sum > max_sum_yagod:
        max_sum_yagod = current_sum

print(gryadka)  
print(max_sum_yagod)
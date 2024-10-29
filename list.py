from statistics import median

fib1 = 0
fib2 = 1
N = input('колличество элементов в ряду фибоначчи: ')
N = int(N)
i = 0
m = [fib1, fib2]
modified = [fib1, fib2]
while i < N - 2: # (N - 2) - потомуто у нас в списке уже имеется 2 элемента
    fib_sum = fib1 + fib2 #-->   (                     )
    fib1 = fib2           #-->  (подсчет числа фибоначчи)
    fib2 = fib_sum        #-->   (                     )    
    i = i + 1   
    m += [fib2]
    if  fib2 % 2 == 0:    # проверка на четность 
        fib2 = fib2 * 2
        modified += [fib2]       # добавление в список
    else:
        fib2 = fib2 ** 2
        modified += [fib2]
    fib2 = fib_sum 

sort = sorted(modified)   #отсортировал список по возрастанию 
med = median(sort) # нахождение медианного значения

rem = [] # создал список
for it in  modified: # прохожусь по каждому элементу
    if  it < med:
        rem = []   
    else:
      rem.append(it) #добавление в конец списка
    if it == med:
        rem.remove(it) # удалил элемент равный медианному значению
sort1 = sorted(rem) #отсортировал список по возрастанию 

length = len(sort1)
a = len(modified) # длина списка

print("список до N",m)
print("преобразованный список:",modified)
print("медианное значени:",med)
print("минимальный элемент:", min(modified))
print("максимальный элемент:", max(modified))
print("длина:", a)
print("количество элементов > медианного значения:", length)
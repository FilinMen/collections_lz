fib1 = 1
fib2 = 2
N = input('колличество элементов в ряду фибоначчи: ')
N = int(N)
i = 0
m = [0, 1, 1, 2]
while i < N - 4:
    fib_sum = fib1 + fib2
    fib1 = fib2
    fib2 = fib_sum
    i = i + 1
    if  fib2 % 2 == 0:
        fib2 = fib2 * 2
        m += [fib2]
    else:
        fib2 = fib2 ** 2
        m += [fib2]
    fib2 = fib_sum
if N % 2 == 0:
    N = N/2
    N =int(N)
    s = m[N:]
else:
    N = (N + 1)/2
    N =int(N)
    s = m[N:]

print("количество элементов > медианного значения:")  
print(len(s))

print("длина:")
print(len(m))

print("минимальный элемент:")
print(min(m))

print("максимальный элемент:")
print(max(m))
print(str(m))

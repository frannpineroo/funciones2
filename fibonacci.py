def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    
    elem1 = elem2 = 1
    sum = 0
    for i in range(3, n + 1):
        sum = elem1 + elem2
        elem1 = elem2
        elem1, elem2 = elem2, sum
    return sum

for n in range(1, 11): #Cuenta de 1 a 10
    print(n, '->', fib(n))
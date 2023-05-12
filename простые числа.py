for a in range(10**7, 10**7+100):
    k = 0
    for i in range(2, a//2+1): # проверка возможных делителей
        if a % i == 0:
            k += 1
        if k > 0:
            break
    if k == 0:
        print(a, end=' ')


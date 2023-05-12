for a in range(110203, 110245+1):
    k = 0
    for i in range(2, a+1):
        if a % i == 0 and (i % 2 == 0):
            k += 1
        if k > 4:
            break
    if k == 4:
       #print(a, end=' ')
       for i in range(2, a + 1):
           if a % i == 0 and i % 2 == 0:
               print(i, end=' ')
       print()


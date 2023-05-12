for a in range(95632,174505  + 1):
    k = 0
    for i in range(1, a+1):
        if a % i == 0:
            if i % 2 != 0:
                k += 1
        if k > 6:
            break
    if k == 6:
        for i in range(1, a + 1):
            if a % i == 0:
                if i % 2 != 0:
                    print(i, end=' ')
        print()


for a in range(100000000, 100000000+1000):
    flag = True
    # for i in range(2, a // 2 + 1):
    for i in range(2, int(a**0.5) + 1):
        if a % i == 0:
            flag = False
            break
    if flag:
        print(a)
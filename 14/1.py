for x in '0123456789ABCDE':
    s1 = int('123' + x + '5', 15)
    s2 = int('1' + x + '233', 15)
    if (s2+s1) % 14 == 0:
        print((s2+s1) // 14)
        break
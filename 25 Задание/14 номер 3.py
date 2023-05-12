for x in '0123456789ABCDEF':
    s1 = int('2' + x + '84', 19)
    s2 = int('2b3' + x, 16)
    if (s2+s1) % 88 == 0:
        print((s2+s1) // 88)
        break
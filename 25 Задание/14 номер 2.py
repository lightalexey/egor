for x in '0123456789ABCDEF':
    s1 = int('28' + x + '2', 18)
    s2 = int('93' + x + '5', 12)
    if (s2+s1) % 133 == 0:
        print((s2+s1) // 133)
        break
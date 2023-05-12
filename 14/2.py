for x in '0123456789ABCD':
    s = int('1' + x + '563', 14) + int('871' + x + '3', 14)
    if s % 24 == 0:
        print(s // 24)
        break
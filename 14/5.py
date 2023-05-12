for x in '0123456789ABC':
    for y in '0123456789ABC':
        n = int('8' + x + '78' + y, 13) + int('79' + x + y + '7', 18)
        if n % 9 == 0:
            print(n//9)
            break
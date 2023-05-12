# ax^2+bx+c=0
a = int(input('введи а='))
b = int(input('введи b='))
c = int(input('введи c='))
D = b ** 2 - 4 * a * c
if D > 0:
    x1 = (-b - D ** (1 / 2)) / 2 / a
    x2 = (-b + D ** (1 / 2)) / 2 / a
    print('x1=', x1)
    print('x2=', x2)
else:
    if D == 0:
        x1 = -b / (2 * a)
        print("x1=x2=", x1)
    else:
        print("нет действительных решений")

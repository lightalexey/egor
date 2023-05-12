# ax+b=0
a = int(input('введи а='))
b = int(input('введи b='))
if a != 0:
    x = -b / a
    print('Корень уравнения равен x=', x)
else: # a=0, уравнение вырождается в уравнение вида b=0
    if b == 0:
        print('x любое')
    else:
        print('решений нет')
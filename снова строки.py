# 1. Вывести все четные цифры
    # 2. Вывести две последние цифры
    # 4. Получить и вывести новое число без первой и последней цифры
n = int(input("Введите число:"))
s = str(n)
for i in range(len(s)):
    if int(s[i]) % 2 == 0:
        print(s[i], end=' ')
print()
for i in s:
    if int(i) % 2 == 0:
        print(i, end='')


#b = s[1::2]
#m = s[-2:]
#k = s[-1]
#h = s[::2]
#j = s[1:-1]
#print(b, m, k, h, j)


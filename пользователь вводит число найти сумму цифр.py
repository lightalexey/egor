n = int(input("Введите число:"))
s = str(n)
k = 0
while(n > 0):
    m = n % 10
    k = k + m
    n = n//10
print("Сумма цифр равна:", k)

# 2 способ
k = 0
for i in range(len(s)):
    k = k + int(s[i])
print(k)

# 3 способ
summa = 0
for i in s:
    summa += int(i)
print(summa)
# =============================================================
# 1. Вывести все четные цифры
# 2. Вывести две последние цифры
    # 3. Вывести две первые цифры
# 4. Получить и вывести новое число без первой и последней цифры
b = s[3:]
print(b)

m = s[:2]#3
print(m)
k = s[0]+s[1]#3
print(k)
print(s[0:2]) #3
print()


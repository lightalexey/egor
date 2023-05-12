a = int(input('введи а='))
k = 0 # количество делителей
for i in range(2, a // 2 + 1):
    if a % i == 0:
        k += 1
        break
if k == 0:
    print("Yes")
else:
    print("No")

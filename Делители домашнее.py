k = 0
for n in range(100,999+1):
    a1 = n // 100
    a2 = n // 10 % 10
    a3 = n % 10
    if a1+a2+a3 == 27:
        k += 1
        print(n)
print(k)

k = 0
n = int(input("введите число:"))
for i in range(1000, 9999+1):
    b1 = i // 1000
    b2 = i // 100 % 10
    b3 = i // 10 % 10
    b4 = i % 10
    if b1+b2+b3+b4 == n:
        k += 1
        print(i)
print(k)


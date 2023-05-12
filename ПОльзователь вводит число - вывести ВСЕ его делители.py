k = 0
n = int(input("введите число:"))
for i in range(1, n+1):
    if n % i == 0:
        print(i)
        k+= 1
print(k)



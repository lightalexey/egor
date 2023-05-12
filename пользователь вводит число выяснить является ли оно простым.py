k = 0
n = int(input("ввести число"))
for i in range(1, n+1):
    if n % i == 0:
        k+=1
if k == 2:
    print("да")
else:
    print("нет")


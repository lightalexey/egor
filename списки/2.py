a = [1, 45, -45, 14, 4, 0, 4, 0, 47, -12]
print(*a)
maximum = a[0]
for i in a:
    if i > maximum:
        maximum = i
min = a[0]
for i in a:
    if i < min:
        min = i
print('max =', maximum, "MINIMUM =", min)
print(max(a))
# print(min(a)) уже работать не будет
max = a[0]
min = a[0]
k =len(a)
for i in range(k):
    if a[i] > max:
        max = a[i]

    if a[i] < min:
        min= a[i]
print("max =", max)
print(min)



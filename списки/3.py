a = [1, 45, -45, 14, 47, 0, 4, 0, 47, -12]
max = a[0]
imax = 0
imin = 0
min = a[0]
k = len(a)
for i in range(k):
    if a[i] > max:
        max = a[i]
        imax = i
    if a[i] < min:
        min= a[i]
        imin = i
print(max, min)
print(imax, imin)


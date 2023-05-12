a = [1, 45, -45, 14, 47, 0, 4, 0, 47, -12]
imax = 0
imin = 0
k = len(a)
for i in range(k):
    if a[i] > a[imax]:
        imax = i
    if a[i] < a[imin]:        
        imin = i
print(a[imax], a[imin])
print(imax, imin)

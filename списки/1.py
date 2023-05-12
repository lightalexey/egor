a = [1, 45, -45, 14, 4, 0, 4, 0, 47, -12]
n = len(a)
print(a[0], n, a[n-1], a[-1])

summa = 0
p = 1
for i in a:
    summa += i
    if i != 0:
        p *= i
print(summa)
print(p)

summa = 0
p = 1
for i in range(n):
    summa += a[i]
    if a[i]!= 0:
        p *= a[i]
print(summa, p)
print(sum(a))
print(summa/n)

sump = 0
for i in range(n):
    if a[i] > 0:
        sump += a[i]
print(sump)

sump = 0
polog=0
for i in a:
    if i > 0:
        sump += i
        polog += 1
print(sump)
print(sump/polog)

nol = 0
for i in range(n):
    if a[i] == 0:
        nol = nol + 1
print(nol)

nol = 0
for i in a:
    if i == 0:
        nol += 1
print(nol)

chet=0
for i in a:
    if a % 2 == 0:
        chet +=1
print(chet)











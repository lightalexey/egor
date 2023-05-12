a = [1, 4, 5, 1, 7, 0, 4, 0, 4, 5]
# количество пар соседних элементов, сумма которых четна
k = 0
for i in range(len(a)-1):
    if (a[i] + a[i+1]) % 2 == 0:
        k += 1
print(k)
# количество пар соседних элементов, где оба элементы четны
k = 0
for i in range(len(a)-1):
    if a[i] % 2 == 0 and a[i+1] % 2 == 0:
        k += 1
print(k)
# количество пар соседних элементов, где хотя бы один делится на 5
k = 0
for i in range(len(a)-1):
    if a[i] % 5 == 0 or a[i+1] % 5 ==0:
        k +=1
print(k)

# количество пар соседних элементов, произведение которых четно, и хотя бы один элемент нечетный
k = 0
for i in range(len(a)-1):
    if (a[i] * a[i+1]) % 2  == 0 and (a[i] % 2 != 0 or a[i+1] % 2 !=0):
        k += 1
print(k)
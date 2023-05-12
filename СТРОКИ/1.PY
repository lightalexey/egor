s = 'мама мыла раму!'
print(s[0], len(s), s[len(s)-1], s[-1])
# s[0] = 'М' : Так работать не будет
s = s.replace('м', 'М', 1)
print(s)
print(s[4:])
s = 'Папа' + s[4:]
print(s)
s = s.replace('мыла', 'мыл', 1)
print(s)
k_a = 0
for i in range(len(s)):
    if s[i] == 'а':
        k_a += 1
print(k_a)

k_a = 0
for i in s:
    if i == 'а':
        k_a += 1
print(k_a)
k_a = s.count('а')
print(k_a)
print(s.count('а'))

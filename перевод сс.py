n = int(input("число"))
b = int(input("система счисления "))
m = ''
while n > 0:
    m = str(n % b) + m
n //= b
print(m)

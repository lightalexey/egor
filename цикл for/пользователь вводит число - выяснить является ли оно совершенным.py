# 6 = 1 + 2 +3
# 28 = 1 + 2 + 4 + 7 + 14
a = int(input())
s = 0
for d in range(1, a//2+1):
        if a % d == 0:
            s += d
if s == a:
     print('yes')
else:
     print('no')
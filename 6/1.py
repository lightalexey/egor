k = 0
for x in range(1, 10):
    for y in range(1, 10):
        if y > 3**(-0.5) * x and y < -3**(-0.5) * x + 10:
            k = k + 1
print(k)